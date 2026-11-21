
from pathlib import Path
from model import predict_sales

prediction = predict_sales(100)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>MLOps CI/CD Demo</title>
</head>
<body>
    <h1>MLOps CI/CD Demo</h1>
    <h2>Prediction Result: {prediction}</h2>
    <p>Automatically deployed using GitHub Actions.</p>
</body>
</html>
"""

Path("site").mkdir(exist_ok=True)
Path("site/index.html").write_text(html, encoding="utf-8")