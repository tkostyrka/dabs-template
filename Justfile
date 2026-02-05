commit msg:
    @echo "Committing with message: {{msg}}"
    git pull
    git add .
    git commit -m "{{msg}}"
    git push
