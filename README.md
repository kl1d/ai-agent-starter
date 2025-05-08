# 🧠 AI Agent Starter Kit

An AI-powered agent starter kit that provides a foundational structure to develop AI agents using **LangChain**, **Flask**, **Docker**, and **OpenAI**. This project serves as a template for building AI agents, demonstrating a concrete example by generating SQL statements from natural language queries.

## 🚀 Features

1. **Agent Starter Code:** A reusable template for creating AI agents with multiple task handling.
2. **SQL Generation Example:** Uses natural language to generate SQL queries as a demonstration of agent capabilities.
3. **SQL Validation:** Verifies the generated SQL statements for correctness.
4. **SQL Execution:** Runs the SQL queries against a SQLite database.
5. **Interactive Web UI:** A simple interface to input queries and view agent responses and logs.
6. **Detailed Agent Logs:** Track each step taken by the agent, from query generation to execution.

## 🛠️ Project Structure

```
ai-agent-starter/
├── agent/
│   ├── __init__.py
│   └── agent.py        # AI agent logic
├── web/
│   ├── templates/
│   │    └── index.html # Frontend web UI
│   ├── app.py          # Flask application
│   └── requirements.txt
├── data/
│   └── sample.db       # SQLite database
├── init_db.sh          # DB initialization script
├── Dockerfile
├── docker-compose.yml
├── .env                # API keys and configuration
└── README.md
```

## 📝 Prerequisites

* Docker and Docker Compose installed
* OpenAI API key (get it from [OpenAI](https://platform.openai.com/))

## 🌟 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-agent-starter.git
cd ai-agent-starter
```

### 2. Create a `.env` File

Add your OpenAI API key:

```
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXX
```

### 3. Build and Run the Docker Containers

```bash
docker-compose up --build
```

### 4. Access the Web UI

Visit:

```
http://localhost:5000/
```

### 5. Test with a Query

Try something like:

```
Show me customers who spent more than 1000.
```

## 💻 Usage

* **Input:** Natural language query, e.g., "List all customers who spent more than \$1000 last month."
* **Output:**

  * Generated SQL query
  * SQL validation result
  * Query execution output
* **Logs:** View the agent's thought process and each step in real-time.

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request
