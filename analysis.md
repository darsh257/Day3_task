# Day 1 – From Prompt to Action

## 1. Scenario

I created a **College Course Fee Assistant**. It answers general questions about course fees and uses one tool, `get_course_fee()`, to find the fee of a specific course.

Example:

```text
get_course_fee("AI202")
→ The fee for AI202 is ₹18,000.
```

---

## 2. What is an LLM?

A Large Language Model (LLM) is an AI model trained on a large amount of text. It can understand questions and generate answers based on its learned knowledge and the information given in the prompt.

For example, it can answer:

> What is a course fee?

However, it cannot reliably know private or current information that is not provided to it. For example, it cannot automatically access my course-fee database to find the fee of `AI202`.

---

## 3. What is an AI Agent?

An AI agent is an LLM that can use external tools to complete tasks.

A plain LLM works like:

```text
Question → LLM → Answer
```

An agent can work like:

```text
Question → LLM → Tool → Result → LLM → Answer
```

In my project, the agent decides to use `get_course_fee()` when the user asks for a specific course fee.

---

## 4. What is a Tool and Tool Call?

A **tool** is an external function that gives the LLM an ability it does not have by itself.

My tool is:

```text
get_course_fee(course_code)
```

The tool schema tells the LLM:

* Tool name
* What the tool does
* Required parameters
* Parameter types

A **tool call** is the request made by the LLM to use that function.

Example:

```text
get_course_fee("AI202")
```

The LLM needs the tool description so it knows **when to use the tool and what information to provide**.

---

## 5. Tool Call Flow

For the question:

> What is the fee for AI202?

The process is:

```text
1. User asks the question.
2. LLM understands that a specific fee is required.
3. LLM decides to use the tool.
4. Tool call: get_course_fee("AI202")
5. Tool returns: ₹18,000.
6. LLM receives the result.
7. LLM gives the final answer.
```

Final answer:

> The fee for AI202 is ₹18,000.

---

## 6. Why Return Text on Failure?

A tool should return a message even when something goes wrong.

For example:

```text
No fee information was found for AI999.
```

Instead of crashing the program, this allows the LLM to understand the problem and give a proper response to the user.

---

## 7. Comparison

| Basis                     | Plain LLM         | LLM + Tool                     |
| ------------------------- | ----------------- | ------------------------------ |
| Source                    | Learned knowledge | Knowledge + tool               |
| External information      | No                | Yes                            |
| Specific data reliability | Limited           | Better if tool data is correct |
| Transparency              | Less              | Tool call can be seen          |
| Speed                     | Faster            | Slightly slower                |

---

## 8. Observation

I tested three questions.

| Question                     | Plain LLM                   | Tool-enabled LLM          |
| ---------------------------- | --------------------------- | ------------------------- |
| What is a course fee?        | Answered directly           | Answered without tool     |
| Why do colleges charge fees? | Answered directly           | Answered without tool     |
| What is the fee for AI202?   | No reliable database access | Called `get_course_fee()` |

For the third question, the tool returned:

```text
The fee for AI202 is ₹18,000.
```

The LLM then used this result in its final answer.

---

## 9. Conclusion

A plain LLM is sufficient for general questions and tasks that only require information already available in the prompt or model knowledge.

A tool is useful when the answer requires **external, specific, current, or computed information**.

This experiment demonstrates the basic agent workflow:

```text
Prompt → Decide → Tool Call → Tool Result → Final Answer
```

The main difference is that an agent can **take action using external tools**, while a plain LLM only generates a response from the information available to it.
