conda activate rasa-env
Set-Location -Path .\rasaDemo
Start-Process -FilePath rasa 'run', '--enable-api', '-m', '.\models\', '--cors', '*'