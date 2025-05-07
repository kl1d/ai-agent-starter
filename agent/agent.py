# agent/agent.py
import os
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Logging function to capture intermediate steps
log = []

def log_step(message):
    log.append(message)

# SQL Generator
def sql_generator(query: str) -> str:
    log_step(f"SQL: {query}")
    return f"{query}"

# SQL Validator
def validate_sql(sql: str) -> str:
    log_step(f"Validating SQL: {sql}")
    try:
        # Basic validation: check SQL syntax
        if sql.lower().startswith("select"):
            log_step("SQL is valid.")
            return "SQL is valid."
        log_step("Invalid SQL syntax.")
        return "Invalid SQL syntax."
    except Exception as e:
        log_step(f"Validation Error: {e}")
        return f"Validation Error: {e}"

# SQL Executor
def execute_sql(sql: str) -> str:
    log_step(f"Executing SQL: {sql}")
    try:
        import sqlite3
        conn = sqlite3.connect("/app/data/sample.db")
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        log_step(f"Execution result: {results}")
        return str(results) if results else "No results found."
    except Exception as e:
        log_step(f"Execution Error: {e}")
        return f"Execution Error: {e}"

# Tools for the agent
tools = [
    Tool(name="SQL Generator", func=sql_generator, description="Generates a SQL query from a natural language question. exampe INSERT INTO customers (name, purchase_amount, purchase_date)"),
    Tool(name="SQL Validator", func=validate_sql, description="Validate the syntax of an SQL statement."),
    Tool(name="SQL Executor", func=execute_sql, description="Execute the SQL statement against the database."),
]

# Initialize the agent
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
agent_executor = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True,
    max_iterations=5  # Allow more iterations to capture intermediate steps
)

def get_logs():
    return log
