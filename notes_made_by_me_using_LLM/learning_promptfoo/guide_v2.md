
### The Ultimate Guide to Professional Prompt Engineering with `promptfoo`

Welcome to the definitive guide for transforming your prompt creation process from a guessing game into a rigorous engineering discipline. This guide is tailored for building robust, reliable AI systems like your **NEETPrepGPT** project, where accuracy and consistency are paramount. We'll go from the absolute basics to a fully automated, professional-grade testing workflow.



### Introduction: The Professional Mindset 🧠

In professional AI development, a prompt is not just a question; [cite\_start]**it's a piece of executable code**[cite: 6]. [cite\_start]Like any code, it must be tested[cite: 7]. [cite\_start]Untested prompts lead to unpredictable AI behavior, which is unacceptable for an educational tool where students' careers are on the line[cite: 7, 8].

The fundamental question of prompt engineering is: **How do you *prove* that `Prompt B` is better than `Prompt A`?**

`promptfoo` is the scientific instrument that allows you to answer this question with data, not just feelings. [cite\_start]It helps you systematically verify[cite: 9]:

  * [cite\_start]**Quality & Accuracy:** Does the prompt produce correct, relevant answers? [cite: 10]
  * [cite\_start]**Robustness:** How does it handle tricky questions or edge cases? [cite: 11]
  * [cite\_start]**Consistency:** Does it maintain the desired tone and format? [cite: 12]
  * [cite\_start]**Regression:** Does a new "improvement" accidentally break something that was working before? [cite: 13]

Let's begin.

-----

### Chapter 1: Your First Test - The Core Components 🧪

[cite\_start]The heart of `promptfoo` is a single configuration file: `promptfooconfig.yaml`[cite: 16]. Think of this file as the blueprint for your entire testing operation. It has three core sections.

**1. `prompts`: The "What" You Are Testing**
[cite\_start]This defines the prompt templates you want to evaluate[cite: 19]. A professional best practice is to **never write large prompts directly in the YAML file**. Always load them from external files. [cite\_start]This keeps your configuration clean and your prompts version-controlled like proper code[cite: 25].

```yaml
# promptfooconfig.yaml

prompts:
  - file://prompts/biology_explainer.txt
  - file://prompts/physics_problem_solver.txt
```

**2. `providers`: The "Who" is Being Tested**
[cite\_start]This is where you list the Large Language Models (LLMs) you want to test your prompts against[cite: 31]. [cite\_start]This is incredibly powerful for comparing models like GPT, Claude, and Gemini side-by-side[cite: 33].

```yaml
# promptfooconfig.yaml

providers:
  - id: openai:gpt-4o-mini # Use an ID for clarity when configuring
    config:
      temperature: 0.1 # Lower temp for more predictable, factual answers
  - id: google:gemini-1.5-flash-latest
    config:
      temperature: 0.1
```

**3. `tests`: The "How" You Are Testing**
This is where you define your test cases. [cite\_start]Each case provides variables for your prompt and assertions to check if the output is correct[cite: 48, 49, 50].

Let's tie it all together with a complete first example.

**Your First Test Case:**

  * **File `prompts/biology_explainer.txt`:**
    ```txt
    Explain the biological concept of {{concept}} in simple terms for a NEET aspirant.
    ```
  * **File `promptfooconfig.yaml`:**
    ```yaml
    prompts:
      - file://prompts/biology_explainer.txt

    providers:
      - openai:gpt-4o-mini

    tests:
      - description: "Test basic biology definition of mitosis"
        vars:
          concept: "mitosis"
        assert:
          - type: icontains # Case-insensitive "contains" check
            value: "cell division"
          - type: icontains
            value: "daughter cells"
    ```

To run this, open your terminal and execute:
[cite\_start]`promptfoo eval` [cite: 183]

[cite\_start]This command will run the "mitosis" test case against GPT-4o mini, check if the output contains the required keywords, and show you a pass/fail summary[cite: 184].

-----

### Chapter 2: The Scalability Engine - From One Test to Ten Thousand 🚀

[cite\_start]Manually writing tests in the YAML file is fine for a few cases, but impossible for the thousands needed for a project like NEETPrepGPT[cite: 68]. [cite\_start]The key to professional testing is to **externalize your test data**[cite: 69].

#### Technique 1: The CSV Workhorse

[cite\_start]The most common way to manage a large volume of tests is with a CSV file[cite: 70].

**Step 1: Create `tests/all_subjects.csv`**
[cite\_start]The column headers in your CSV map directly to the `{{variables}}` in your prompt[cite: 74]. You can also define expected outcomes in columns.

```csv
# file: tests/all_subjects.csv
topic,question,expected_keyword_1,expected_keyword_2
"Photosynthesis","What are the two main stages of photosynthesis?","Light-dependent","Calvin cycle"
"Newton's Laws","What is Newton's second law?","Force","mass x acceleration"
"Organic Chemistry","What is the functional group of an alcohol?","Hydroxyl","-OH"
```

**Step 2: Link the CSV in `promptfooconfig.yaml`**
Your `tests` section becomes incredibly simple. [cite\_start]You can point to the entire dataset and create assertions that dynamically use the columns from the CSV for each row[cite: 93].

```yaml
# promptfooconfig.yaml
prompts:
  - 'Answer the following NEET-level question about {{topic}}: {{question}}'

providers:
  - openai:gpt-4o-mini

tests:
  vars: file://tests/all_subjects.csv # Point to the entire test set
  assert:
    # These assertions run for EVERY row in the CSV
    - type: icontains
      value: '{{expected_keyword_1}}' # Dynamically checks the keyword from the CSV!
    - type: icontains
      value: '{{expected_keyword_2}}'
```

#### Technique 2: Google Sheets as a Live, Collaborative Database

For team collaboration, a CSV file can be limiting. You can use a Google Sheet as a live test database that `promptfoo` reads from every time it runs.

1.  [cite\_start]**Create a Google Sheet:** Add headers in the first row that match your variables (e.g., `subject`, `question`, `expected_keyword`)[cite: 204, 205, 207].
2.  [cite\_start]**Share It:** Click `Share` \> `General access` \> `Anyone with the link`[cite: 213, 215]. [cite\_start]This makes it publicly readable, but not editable[cite: 199, 218].
3.  [cite\_start]**Construct the Special URL:** Get your Sheet ID from the normal share link and place it into this template[cite: 222, 225]:
    `https://docs.google.com/spreadsheets/d/SHEET_ID/gviz/tq?tqx=out:csv&sheet=SHEET_NAME`
4.  [cite\_start]**Update `promptfooconfig.yaml`:** Instead of pointing to a local file, use the URL you just constructed[cite: 242].

<!-- end list -->

```yaml
# ... prompts and providers are the same ...

tests:
  # The magic happens here: we point directly to our live Google Sheet URL.
  vars: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/gviz/tq?tqx=out:csv&sheet=Sheet1
  assert:
    - type: icontains
      value: '{{expected_keyword}}' # Checks against the column in the sheet
```

[cite\_start]Now, anyone on your team can add new test cases to the Google Sheet, and they will be automatically included in the next test run without touching any code[cite: 279].

#### How to Design Good Test Cases

Having thousands of tests is useless if they don't cover the right scenarios. For NEETPrepGPT, structure your test bank around this taxonomy:

  * **Factual Recall:** Simple definition checks (e.g., "What is the powerhouse of the cell?").
  * **Conceptual Understanding:** "Why" and "How" questions (e.g., "Explain why ATP is crucial for cellular processes.").
  * **Problem Solving:** Physics and Chemistry numericals that require calculation.
  * **Edge Cases:** Questions with ambiguity or trick details to test robustness.
  * **Negative Testing:** Queries that the AI should refuse to answer (e.g., "How do I cheat on the NEET exam?").

-----

### Chapter 3: The Art of Judgment - Advanced Assertions ⚖️

[cite\_start]Simple keyword checking (`icontains`) is a good start, but it's brittle[cite: 127]. Professional testing requires more sophisticated validation.

**Level 1: Keyword and Regex Matching**

  * **Use Case:** For when the output must contain a very specific, predictable string.
  * **Assertions:** `contains`, `icontains`, `matches` (for regular expressions).

**Level 2: Semantic Similarity (`similar`)**

  * **Use Case:** For when the *meaning* of the output matters more than the exact wording. [cite\_start]There are many ways to correctly define mitosis[cite: 137].
  * [cite\_start]**How it Works:** It checks if the AI's answer is semantically close to your expected answer[cite: 136].
  * **Example:**
    ```yaml
    assert:
      - type: similar
        value: "The process where a cell divides into two identical daughter cells."
        threshold: 0.8 # On a scale of 0 (different) to 1 (identical)
    ```

**Level 3: AI as the Judge (`llm-rubric`)**

  * [cite\_start]**Use Case:** This is a game-changer for evaluating qualities that are hard to define with code: tone, clarity, simplicity, or adherence to complex instructions[cite: 129].
  * [cite\_start]**How it Works:** You use a powerful LLM (like GPT-4o) to grade the output of the model you are testing based on a "rubric" you provide[cite: 129].
  * **Example:** Asserting that an answer is not just correct, but easy for a high school student to understand.
    ```yaml
    assert:
      - type: llm-rubric
        value: "The explanation is simple enough for a high school student to understand and is factually accurate."
        provider: openai:gpt-4o # Use a powerful model for grading
    ```

**Level 4: Ultimate Control (Custom Python/JS Scripts)**

  * **Use Case:** When you need absolute precision that only code can provide. [cite\_start]Perfect for validating numerical answers within a tolerance, checking for a specific JSON structure, or any other custom logic[cite: 143, 144].
  * [cite\_start]**Example:** Checking a physics calculation with a 5% tolerance[cite: 145, 155].
    ```yaml
    # In promptfooconfig.yaml
    assert:
      - type: python
        value: file://validators/validate_physics.py
    ```

-----

### Chapter 4: The Efficiency Toolkit - Pro Techniques 🛠️

#### Combinatorial Testing (The "Matrix Strategy")

What if you want to test 5 different prompts against 3 different models with 100 test cases? That's $5 \* 3 \* 100 = 1500$ total evaluations. `promptfoo` handles this automatically. [cite\_start]This "matrix test" expands your test variables to cover all combinations, giving you massive test coverage with minimal configuration[cite: 110, 126].

  * [cite\_start]**Example:** Test two concepts with three different tones, automatically creating $2 \\times 3 = 6$ tests[cite: 111].
    ```yaml
    prompts:
      - 'In a {{tone}} tone, explain: {{concept}}'
    tests:
      - vars:
          tone: ["simple and direct", "highly technical", "analogy-driven"]
          concept: ["gene expression", "thermodynamics"]
    ```

#### Advanced Templating with Nunjucks

`promptfoo` supports more than just simple `{{variable}}` replacement. You can use Nunjucks templating to add logic like loops and conditionals *inside your prompts*.

  * **Use Case:** Create a more complex prompt structure that changes based on the test case variables. For example, add a "hint" only if one is provided in your CSV.
  * **Example `prompt.txt`:**
    ```nunjucks
    Answer the following question about {{topic}}: {{question}}

    {% if hint %}
    Here is a hint: {{hint}}
    {% endif %}
    ```
    This `{% if hint %}` block will only appear in the final prompt if your CSV row for that test contains a non-empty `hint` column.

#### Managing Cost and Speed

Testing can be slow and expensive. `promptfoo` has built-in features to manage this.

  * **Cost Estimation:** Before running, get a cost estimate.
    `promptfoo eval --view --dry-run`
  * **Caching:** Avoid re-running tests on unchanged prompts. `promptfoo` automatically caches results. This saves a huge amount of time and money.
  * **Concurrency:** Speed up your test runs by making more requests in parallel.
    `promptfoo eval -j 10` (runs 10 tests concurrently)

#### Scoring & Failure Thresholds

[cite\_start]Assertions can produce a score from 0 (fail) to 1 (pass)[cite: 154, 159]. `promptfoo` aggregates these scores. You can configure your evaluation to fail if the overall quality drops below a certain threshold. This is critical for automation.

`promptfoo eval --fail-on-threshold 0.8`

This command will exit with an error code if the overall pass rate is less than 80%, which can be used to block a bad code change in a CI/CD pipeline.

-----

### Chapter 5: The Professional Workflow - From Terminal to Automation ⚙️

Here is the complete, professional workflow.

**1. The Local Loop: Analyze and Iterate**
Your primary development cycle happens locally.

  * [cite\_start]**Run Evaluation:** `promptfoo eval` [cite: 183]
  * **Analyze Results:** The console output is good, but the web viewer is the real power tool. [cite\_start]Run `promptfoo view`[cite: 187].
  * [cite\_start]**The Workbench:** The web viewer opens an interactive dashboard where you can side-by-side compare outputs from different models, filter for failures, and deeply inspect exactly why a test failed[cite: 188, 189]. This is where you will spend most of your time improving your prompts.

**2. The Automated Guardian: CI/CD Integration**
[cite\_start]For a truly professional setup, integrate `promptfoo` into your Continuous Integration/Continuous Deployment pipeline (e.g., GitHub Actions)[cite: 192]. [cite\_start]This acts as an automated regression test for your prompts[cite: 194].

  * [cite\_start]**How it Works:** You can create a workflow that automatically runs `promptfoo eval` every time a developer tries to merge a change to a prompt file[cite: 193].
  * **Example GitHub Actions Step:**
    ```yaml
    - name: Run Promptfoo Regression Tests
      run: |
        npm install -g promptfoo
        promptfoo eval --fail-on-threshold 0.9 --no-progress-bar
    ```
    [cite\_start]If the test pass rate drops below 90%, the workflow will fail, **preventing the merge** and ensuring that a bad prompt change never makes it into your application[cite: 195].

-----

### Conclusion: From Artisan to Engineer

[cite\_start]By following this guide, you have moved from ad-hoc prompt writing to a systematic engineering discipline[cite: 196]. [cite\_start]You are now equipped to design, execute, and analyze thousands of tests, ensuring your **NEETPrepGPT** project is built on a foundation of measurable quality and reliability[cite: 197]. This structured, data-driven approach is what separates amateur results from professional-grade AI.