(() => {
  const modes = {
    scientific: [
      ["sin + sqrt", "sin(pi / 2) + sqrt(16)"],
      ["log base 10", "log(100, 10)"],
      ["factorial", "factorial(5)"],
    ],
    basic: [
      ["order of operations", "(12 + 8) * 3"],
      ["power", "2 ** 10"],
      ["round", "round(10 / 3, 2)"],
    ],
    programmer: [
      ["binary AND", "0b1010 & 0b1100"],
      ["hex addition", "0xFF + 1"],
      ["shift left", "7 << 2"],
    ],
  };

  const functions = {
    basic: { abs: Math.abs, round: Math.round, sqrt: Math.sqrt, pow: Math.pow },
    scientific: {
      abs: Math.abs, acos: Math.acos, asin: Math.asin, atan: Math.atan,
      ceil: Math.ceil, cos: Math.cos, exp: Math.exp, floor: Math.floor,
      log: (value, base) => base === undefined ? Math.log(value) : Math.log(value) / Math.log(base),
      log10: Math.log10, log2: Math.log2, max: Math.max, min: Math.min,
      pow: Math.pow, round: Math.round, sin: Math.sin, sqrt: Math.sqrt,
      tan: Math.tan, trunc: Math.trunc,
      cbrt: Math.cbrt || (value => Math.sign(value) * Math.abs(value) ** (1 / 3)),
      factorial: value => {
        if (!Number.isInteger(value) || value < 0 || value > 170) throw new Error("factorial expects an integer from 0 to 170");
        let result = 1;
        for (let number = 2; number <= value; number += 1) result *= number;
        return result;
      },
    },
    programmer: {},
  };

  const tokenize = expression => {
    const source = expression.trim();
    if (!source || source.length > 160) throw new Error("Enter an expression up to 160 characters.");
    const pattern = /\s*(0[xX][\da-fA-F]+|0[bB][01]+|0[oO][0-7]+|(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?|[A-Za-z_]\w*|<<|>>|\*\*|[()+\-*/%,&|^~])/y;
    const tokens = [];
    let position = 0;
    while (position < source.length) {
      pattern.lastIndex = position;
      const match = pattern.exec(source);
      if (!match) throw new Error(`Unsupported input near "${source.slice(position, position + 12)}".`);
      tokens.push(match[1]);
      position = pattern.lastIndex;
      if (tokens.length > 100) throw new Error("Expression is too complex.");
    }
    return tokens;
  };

  const calculate = (expression, mode) => {
    const tokens = tokenize(expression);
    const available = functions[mode];
    let cursor = 0;
    const peek = () => tokens[cursor];
    const take = () => tokens[cursor++];
    const match = expected => peek() === expected ? Boolean(take()) : false;
    const safeInteger = value => {
      if (!Number.isSafeInteger(value)) throw new Error("Bitwise operations require safe integers.");
      return value;
    };
    const checked = value => {
      if (typeof value !== "number" || !Number.isFinite(value) || Math.abs(value) > 1e100) {
        throw new Error("The result is outside the supported numeric range.");
      }
      return value;
    };

    const primary = () => {
      const token = take();
      if (token === undefined) throw new Error("Expression is incomplete.");
      if (token === "(") {
        const value = bitOr();
        if (!match(")")) throw new Error("Add a closing parenthesis.");
        return value;
      }
      if (/^(?:0[xX]|0[bB]|0[oO])/.test(token)) {
        const value = Number(token);
        if (!Number.isSafeInteger(value)) throw new Error("Integer literal is too large.");
        return value;
      }
      if (/^(?:\d|\.)/.test(token)) {
        const value = Number(token);
        if (!Number.isFinite(value)) throw new Error("Enter a finite number.");
        if (mode === "programmer" && !Number.isSafeInteger(value)) throw new Error("Programmer mode accepts integer values only.");
        return value;
      }
      if (/^[A-Za-z_]/.test(token)) {
        if (match("(")) {
          const args = [];
          if (!match(")")) {
            do { args.push(bitOr()); } while (match(","));
            if (!match(")")) throw new Error("Add a closing parenthesis.");
          }
          if (!Object.hasOwn(available, token)) throw new Error(`"${token}" is not available in ${mode} mode.`);
          return checked(available[token](...args));
        }
        if (mode !== "programmer") {
          const constants = { e: Math.E, pi: Math.PI, tau: 2 * Math.PI };
          if (Object.hasOwn(constants, token)) return constants[token];
        }
        throw new Error(`Unknown name "${token}".`);
      }
      throw new Error(`Unexpected token "${token}".`);
    };

    const power = () => {
      let value = primary();
      if (match("**")) value = checked(value ** unary());
      return value;
    };
    const unary = () => {
      if (match("+")) return unary();
      if (match("-")) return -unary();
      if (match("~")) {
        if (mode !== "programmer") throw new Error("Bitwise operators are available in programmer mode.");
        return ~safeInteger(unary());
      }
      return power();
    };
    const term = () => {
      let value = unary();
      while (["*", "/", "%"].includes(peek())) {
        const operator = take();
        const right = unary();
        if ((operator === "/" || operator === "%") && right === 0) throw new Error("Division by zero.");
        value = checked(operator === "*" ? value * right : operator === "/" ? value / right : value % right);
      }
      return value;
    };
    const addition = () => {
      let value = term();
      while (peek() === "+" || peek() === "-") {
        const operator = take();
        const right = term();
        value = checked(operator === "+" ? value + right : value - right);
      }
      return value;
    };
    const shifts = () => {
      let value = addition();
      while (peek() === "<<" || peek() === ">>") {
        if (mode !== "programmer") throw new Error("Bitwise operators are available in programmer mode.");
        const operator = take();
        const amount = safeInteger(addition());
        if (amount < 0 || amount > 31) throw new Error("Shift amount must be between 0 and 31.");
        value = operator === "<<" ? safeInteger(value) << amount : safeInteger(value) >> amount;
      }
      return value;
    };
    const bitAnd = () => {
      let value = shifts();
      while (match("&")) {
        if (mode !== "programmer") throw new Error("Bitwise operators are available in programmer mode.");
        value = safeInteger(value) & safeInteger(shifts());
      }
      return value;
    };
    const bitXor = () => {
      let value = bitAnd();
      while (match("^")) {
        if (mode !== "programmer") throw new Error("Bitwise operators are available in programmer mode.");
        value = safeInteger(value) ^ safeInteger(bitAnd());
      }
      return value;
    };
    const bitOr = () => {
      let value = bitXor();
      while (match("|")) {
        if (mode !== "programmer") throw new Error("Bitwise operators are available in programmer mode.");
        value = safeInteger(value) | safeInteger(bitXor());
      }
      return value;
    };

    const result = bitOr();
    if (cursor !== tokens.length) throw new Error(`Unexpected token "${peek()}".`);
    return result;
  };

  const initTheme = () => {
    const root = document.documentElement;
    let preference = "dark";
    try {
      const stored = localStorage.getItem("calcservice-theme");
      if (stored === "dark" || stored === "light") preference = stored;
    } catch {
      preference = "dark";
    }
    root.dataset.theme = preference;
    const themeColor = document.querySelector('meta[name="theme-color"]');
    document.querySelectorAll(".theme-toggle").forEach(button => {
      const update = () => {
        const isDark = root.dataset.theme === "dark";
        if (themeColor) themeColor.content = isDark ? "#090e16" : "#f5f7f8";
        button.setAttribute("aria-label", `Switch to ${isDark ? "light" : "dark"} theme`);
        button.title = `Switch to ${isDark ? "light" : "dark"} theme`;
        const glyph = button.querySelector(".theme-glyph");
        if (glyph) glyph.textContent = isDark ? "☼" : "◐";
      };
      update();
      button.addEventListener("click", () => {
        root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
        try { localStorage.setItem("calcservice-theme", root.dataset.theme); } catch { /* Theme still works for this page. */ }
        update();
      });
    });
  };

  const initMobileNavigation = () => {
    const toggle = document.querySelector(".menu-toggle");
    const navigation = document.querySelector(".primary-nav");
    if (!toggle || !navigation) return;
    const close = () => {
      toggle.setAttribute("aria-expanded", "false");
      toggle.setAttribute("aria-label", "Open navigation");
      navigation.classList.remove("open");
    };
    toggle.addEventListener("click", () => {
      const opening = toggle.getAttribute("aria-expanded") !== "true";
      toggle.setAttribute("aria-expanded", String(opening));
      toggle.setAttribute("aria-label", opening ? "Close navigation" : "Open navigation");
      navigation.classList.toggle("open", opening);
    });
    navigation.addEventListener("click", event => {
      if (event.target.closest("a")) close();
    });
    document.addEventListener("keydown", event => {
      if (event.key === "Escape") close();
    });
    document.addEventListener("click", event => {
      if (!navigation.contains(event.target) && !toggle.contains(event.target)) close();
    });
  };

  const initMotion = () => {
    const elements = document.querySelectorAll(".reveal");
    if (!elements.length || window.matchMedia("(prefers-reduced-motion: reduce)").matches || !("IntersectionObserver" in window)) {
      elements.forEach(element => element.classList.add("is-visible"));
      return;
    }
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -36px 0px", threshold: .08 });
    elements.forEach((element, index) => {
      if (element.classList.contains("tool-card") || element.classList.contains("community-card")) {
        element.style.transitionDelay = `${(index % 4) * 55}ms`;
      }
      observer.observe(element);
    });
  };

  const initPlayground = () => {
    const form = document.querySelector("#demo-form");
    const input = document.querySelector("#demo-expression");
    if (!form || !input) return;
    let mode = "scientific";
    const result = document.querySelector("#demo-result");
    const output = document.querySelector(".demo-output");
    const error = document.querySelector("#demo-error");
    const caption = document.querySelector("#mode-caption");
    const status = document.querySelector("#demo-status");
    const exampleContainer = document.querySelector(".demo-examples");

    const refreshExamples = () => {
      const fragment = document.createDocumentFragment();
      modes[mode].forEach(([label, expression]) => {
        const button = document.createElement("button");
        button.type = "button";
        button.dataset.expression = expression;
        button.textContent = label;
        fragment.append(button);
      });
      exampleContainer.replaceChildren(fragment);
    };

    const run = () => {
      try {
        const value = calculate(input.value, mode);
        result.textContent = Object.is(value, -0) ? "0" : String(value);
        error.textContent = "";
        output.classList.remove("error");
        status.textContent = "CALCULATED";
        output.classList.remove("calculated");
        void output.offsetWidth;
        output.classList.add("calculated");
      } catch (problem) {
        result.textContent = "—";
        error.textContent = problem instanceof Error ? problem.message : "Unable to calculate this expression.";
        output.classList.add("error");
        status.textContent = "CHECK INPUT";
      }
    };

    document.querySelector(".demo-tabs")?.addEventListener("click", event => {
      const button = event.target.closest("[data-mode]");
      if (!button) return;
      mode = button.dataset.mode;
      document.querySelectorAll(".demo-tab").forEach(tab => {
        const selected = tab === button;
        tab.classList.toggle("active", selected);
        tab.setAttribute("aria-pressed", String(selected));
      });
      caption.textContent = mode === "scientific" ? "· radians" : mode === "programmer" ? "· integer & bitwise" : "· arithmetic";
      input.value = modes[mode][0][1];
      error.textContent = "";
      refreshExamples();
      run();
    });

    exampleContainer?.addEventListener("click", event => {
      const button = event.target.closest("[data-expression]");
      if (!button) return;
      input.value = button.dataset.expression;
      run();
      input.focus();
    });

    form.addEventListener("submit", event => {
      event.preventDefault();
      run();
    });
    input.addEventListener("input", () => {
      error.textContent = "";
      output.classList.remove("error");
    });
    run();
  };

  const initCopyButtons = () => {
    document.querySelectorAll("[data-copy]").forEach(button => {
      button.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(button.dataset.copy);
          const original = button.dataset.originalLabel || button.textContent;
          button.dataset.originalLabel = original;
          button.textContent = "COPIED";
          window.setTimeout(() => { button.textContent = original; }, 1400);
        } catch {
          button.textContent = "COPY FAILED";
          window.setTimeout(() => { button.textContent = button.dataset.originalLabel || "COPY"; }, 1600);
        }
      });
    });
  };

  const initReadingProgress = () => {
    if (!document.querySelector(".guide-content")) return;
    const meter = document.createElement("div");
    meter.className = "reading-progress";
    meter.setAttribute("aria-hidden", "true");
    meter.innerHTML = "<span></span>";
    document.body.append(meter);
    const fill = meter.firstElementChild;
    let queued = false;
    const update = () => {
      const scrollable = document.documentElement.scrollHeight - window.innerHeight;
      const ratio = scrollable > 0 ? Math.min(window.scrollY / scrollable, 1) : 0;
      fill.style.width = `${ratio * 100}%`;
      queued = false;
    };
    window.addEventListener("scroll", () => {
      if (!queued) {
        queued = true;
        window.requestAnimationFrame(update);
      }
    }, { passive: true });
    update();
  };

  const initBackToTop = () => {
    let buttons = [...document.querySelectorAll(".back-top")];
    if (!buttons.length) {
      const button = document.createElement("button");
      button.className = "back-top";
      button.type = "button";
      button.setAttribute("aria-label", "Back to top");
      button.textContent = "↑";
      document.body.append(button);
      buttons = [button];
    }
    buttons.forEach(button => {
      button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    });
    document.querySelectorAll(".footer-back-top").forEach(button => {
      button.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));
    });
    const update = () => buttons.forEach(button => button.classList.toggle("visible", window.scrollY > 450));
    window.addEventListener("scroll", update, { passive: true });
    update();
  };

  const initGuideNavigation = () => {
    const links = [...document.querySelectorAll(".guide-rail a[href^='#']")];
    if (!links.length || !("IntersectionObserver" in window)) return;
    const sections = links.map(link => document.querySelector(link.getAttribute("href"))).filter(Boolean);
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      links.forEach(link => {
        const active = link.getAttribute("href") === `#${visible.target.id}`;
        link.classList.toggle("active", active);
        if (active) link.setAttribute("aria-current", "location");
        else link.removeAttribute("aria-current");
      });
    }, { rootMargin: "-18% 0px -67% 0px", threshold: 0 });
    sections.forEach(section => observer.observe(section));
  };

  const initPointerEffects = () => {
    if (!window.matchMedia("(hover: hover) and (pointer: fine)").matches || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const cursor = document.createElement("div");
    cursor.className = "cursor-aura";
    cursor.setAttribute("aria-hidden", "true");
    document.body.append(cursor);
    let x = window.innerWidth / 2;
    let y = window.innerHeight / 2;
    let targetX = x;
    let targetY = y;
    let frame = 0;
    let active = false;
    const paint = () => {
      x += (targetX - x) * .18;
      y += (targetY - y) * .18;
      cursor.style.transform = `translate3d(${x}px, ${y}px, 0) translate(-50%, -50%)`;
      if (Math.abs(targetX - x) > .15 || Math.abs(targetY - y) > .15) {
        frame = window.requestAnimationFrame(paint);
      } else {
        frame = 0;
      }
    };
    window.addEventListener("pointermove", event => {
      targetX = event.clientX;
      targetY = event.clientY;
      if (!active) {
        active = true;
        cursor.classList.add("active");
      }
      if (!frame) frame = window.requestAnimationFrame(paint);
    }, { passive: true });
    document.addEventListener("pointerover", event => {
      const target = event.target.closest("a, button, input, summary, .tool-card, .community-card");
      cursor.classList.toggle("hovering", Boolean(target));
    });
    window.addEventListener("blur", () => {
      active = false;
      cursor.classList.remove("active", "hovering");
    });
    document.querySelectorAll(".tool-card, .community-card, .demo-window").forEach(card => {
      card.addEventListener("pointermove", event => {
        const bounds = card.getBoundingClientRect();
        card.style.setProperty("--pointer-x", `${event.clientX - bounds.left}px`);
        card.style.setProperty("--pointer-y", `${event.clientY - bounds.top}px`);
      }, { passive: true });
    });
  };

  const initTerminalAnimation = () => {
    const expression = document.querySelector("#hero-expression");
    const result = document.querySelector("#hero-result");
    const mode = document.querySelector("#hero-mode");
    const modeBadge = document.querySelector("#hero-mode-badge");
    const modeStatus = document.querySelector("#hero-mode-status");
    if (!expression || !result || !mode || !modeBadge || !modeStatus || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    const examples = [
      ["scientific", "sin(pi / 2) + sqrt(16)", "5.0"],
      ["programmer", "0xFF + 1", "256"],
      ["basic", "(12 + 8) * 3", "60"],
      ["scientific", "factorial(5)", "120"],
    ];
    let current = 0;
    window.setInterval(() => {
      current = (current + 1) % examples.length;
      expression.classList.add("changing");
      result.classList.add("changing");
      window.setTimeout(() => {
        mode.textContent = examples[current][0];
        modeBadge.textContent = examples[current][0].toUpperCase();
        modeStatus.textContent = examples[current][0] === "scientific" ? "PRECISION MODE" : examples[current][0] === "programmer" ? "INTEGER MODE" : "EVERYDAY MODE";
        expression.textContent = examples[current][1];
        result.firstChild.textContent = examples[current][2];
        expression.classList.remove("changing");
        result.classList.remove("changing");
      }, 240);
    }, 4200);
  };

  const initNavigation = () => {
    const main = document.querySelector("main");
    const progress = document.createElement("div");
    progress.className = "scroll-progress";
    progress.setAttribute("aria-hidden", "true");
    progress.innerHTML = "<span></span>";
    document.body.prepend(progress);
    const bar = progress.firstElementChild;
    let queued = false;
    const update = () => {
      const available = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = `${available > 0 ? Math.min(window.scrollY / available, 1) * 100 : 0}%`;
      queued = false;
    };
    window.addEventListener("scroll", () => {
      if (!queued) {
        queued = true;
        window.requestAnimationFrame(update);
      }
    }, { passive: true });
    window.addEventListener("resize", update, { passive: true });
    update();
    main?.classList.add("page-enter");
  };

  const init = () => {
    initTheme();
    initMobileNavigation();
    initNavigation();
    initMotion();
    initPlayground();
    initCopyButtons();
    initReadingProgress();
    initBackToTop();
    initGuideNavigation();
    initPointerEffects();
    initTerminalAnimation();
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init, { once: true });
  else init();
})();
