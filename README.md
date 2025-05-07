# 🧠 AI Agent Starter Kit for SQL Query Generation

An AI-powered agent that converts natural language queries into SQL statements, validates them, and executes them against a SQLite database. Built with **LangChain**, **Flask**, **Docker**, and **OpenAI**.

---

## 🚀 Features
1. **SQL Generation:** Converts natural language to SQL.
2. **SQL Validation:** Verifies the correctness of the SQL statement.
3. **SQL Execution:** Runs the SQL against a SQLite database.
4. **Interactive Web UI:** Input natural language queries and view results and logs.
5. **Detailed Agent Logs:** Track each step taken by the agent.

---

## 🛠️ Project Structure
```

ai-agent-starter/
├── agent/
│   ├── **init**.py
│   └── agent.py        # AI agent logic
├── web/
│   ├── templates/
│   │    └── index.html # Frontend web UI
│   ├── app.py          # Flask application
│   └── requirements.txt
├── data/
│   └── sample.db       # SQLite database
├── init\_db.sh          # DB initialization script
├── Dockerfile
├── docker-compose.yml
├── .env                # API keys and configuration
└── README.md

````

---

## 📝 Prerequisites
- Docker and Docker Compose installed
- OpenAI API key (get it from [OpenAI](https://platform.openai.com/))

---

## 🌟 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/kl1d/ai-agent-starter.git
cd ai-agent-starter
````

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

---

## 💻 Usage

* **Input:** Natural language query, e.g., "List all customers who spent more than \$1000 last month."
* **Output:**

  * Generated SQL query
  * SQL validation result
  * Query execution output
* **Logs:** View the agent's thought process and each step in real-time.

---

## 🛠️ Development

### Updating Dependencies

If you add new Python packages, update `web/requirements.txt`:

```bash
pip freeze > web/requirements.txt
```

### Rebuilding the Docker Image

```bash
docker-compose up --build
```

---

## 🐛 Troubleshooting

### Issue: Port Already In Use

Stop any existing containers running on port 5000:

```bash
docker ps
docker stop <container_id>
```

### Issue: Agent Iteration Limit

The agent might reach its iteration limit if the query is too complex. Increase the iteration limit in `agent.py`:

```python
max_iterations=5
```

---

## 🗃️ Database Initialization

The database is automatically created when the container starts. To manually initialize:

```bash
docker exec -it ai_agent_app sqlite3 /app/data/sample.db
```

### Checking the Database

```sql
SELECT * FROM customers;
```

---

## 🤖 Technologies Used

* **LangChain**: Agent orchestration
* **Flask**: Web application framework
* **OpenAI API**: Natural language understanding
* **SQLite**: Lightweight database
* **Docker**: Containerization

---

## 📝 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! Please follow these steps:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---
