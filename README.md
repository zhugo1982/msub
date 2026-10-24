

```
command -v python3 >/dev/null || (apt-get update -y && apt-get install -y python3); curl -sSL https://raw.githubusercontent.com/你的用户名/仓库名/refs/heads/main/msub.py -o /usr/local/bin/msub && chmod +x /usr/local/bin/msub; msub
```
