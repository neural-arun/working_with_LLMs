

**Topic:** `<INSERT TOPIC HERE>`

> Goal: Understand this topic as a **system designer**, not as a syntax memorizer.

---

## 1️⃣ WHY — Why does this exist? (System Purpose)

**Real-world problem it solves:**

* What pain existed before this concept?
* What breaks if this concept does NOT exist?

**Plain example (non-technical):**

* Explain it using a real-life situation (bank, traffic, school, factory, etc.)

**Key question to ask:**

> “If I remove this from the system, what becomes impossible or unsafe?”

---

## 2️⃣ WHERE — Where does it live inside a system?

This concept usually belongs to **one main role**:

* 🔁 **Flow** — controls how things move
* 📦 **State** — stores or remembers data
* 🧭 **Control** — decides what happens next
* 🚧 **Boundary** — protects system edges (input/output)
* 🧠 **Responsibility** — who does what

**Answer clearly:**

* Which role does `<INSERT TOPIC HERE>` play?
* What does it *touch*?
* What should it *never* touch?

**Simple system diagram (mental):**

```
Input → [ THIS CONCEPT ] → Output
```

---

## 3️⃣ WHAT CAN GO WRONG — Failure modes (very important)

**Common mistakes beginners make:**

* What do people misuse?
* What do they overuse?
* What do they forget to handle?

**Real failure examples:**

* What breaks in production?
* What causes bugs, crashes, or wrong data?

**Good system response:**

* How should a **well-designed system** handle these failures?
* Ignore? Validate? Fail loudly? Recover?

> A designer thinks:
> “How does the system behave when things go wrong?”

---

## 4️⃣ HOW — Minimal Python mechanism (only essentials)

⚠️ **Rules here:**

* No memorization
* No advanced tricks
* Only the smallest working idea

**Core mechanism (1–2 ideas max):**

* What Python feature enables this?
* What is the *one thing* Python is doing here?

**Tiny example (focus on idea, not syntax):**

```python
# minimal example that shows the core idea
```

**Explain in words:**

* What enters?
* What happens?
* What leaves?

---

## 5️⃣ WHO — Ownership & responsibility

**Who SHOULD handle this:**

* Library code?
* Core logic?
* Edge/boundary code?
* User input layer?

**Who should NOT handle this:**

* Business logic?
* UI?
* Random helper functions?

**Design rule:**

> “If I put this in the wrong place, what damage does it cause?”

---

## 🧠 One-Line Mental Model

> **`<INSERT TOPIC HERE>` is basically:**
> **“____________________________________.”**

(Example structure:
“a gate that decides…”,
“a container that guarantees…”,
“a guard that prevents…”)

---

