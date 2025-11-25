import pdfplumber
import spacy
import re
import json

# 加载中文模型
nlp = spacy.load("zh_core_web_sm")

# 1. 提取纯文本
def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# 2. 正则+NER 解析关键字段
def parse_resume(text: str):
    data = {
        "name": None,
        "phone": None,
        "email": None,
        "education": [],
        "skills": [],
        "experience": []
    }

    # 电话
    phone_match = re.search(r"(1[3-9]\d{9})", text)
    if phone_match:
        data["phone"] = phone_match.group(1)

    # 邮箱
    email_match = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
    if email_match:
        data["email"] = email_match.group(0)

    # 姓名（简单策略：第一行非空且长度2-4的中文字符）
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if lines:
        first = lines[0]
        if re.fullmatch(r"[\u4e00-\u9fa5]{2,4}", first):
            data["name"] = first

    # 技能（关键词表）
    skill_keywords = {
        "Python", "Django", "Flask", "Redis", "MySQL", "PostgreSQL",
        "Docker", "Kubernetes", "微服务", "高并发", "Spring", "Go", "Java"
    }
    found_skills = {kw for kw in skill_keywords if kw in text}
    data["skills"] = list(found_skills)

    # 教育（正则）
    edu_pattern = re.compile(r"(\w+大学|学院).*?(本科|硕士|博士).*?(\d{4})")
    for m in edu_pattern.finditer(text):
        data["education"].append({
            "school": m.group(1),
            "degree": m.group(2),
            "year": m.group(3)
        })

    # 工作经历（简易）
    exp_pattern = re.compile(r"(\d{4}\.\d{2}).*?(\d{4}\.\d{2}|至今)\s+(\w+公司)\s+(\w+)")
    for m in exp_pattern.finditer(text):
        data["experience"].append({
            "period": f"{m.group(1)}–{m.group(2)}",
            "company": m.group(3),
            "role": m.group(4)
        })

    return data

# 3. 主函数
if __name__ == "__main__":
    pdf_path = "resume_zhangsan.pdf"   # 换成你的文件
    text = extract_text(pdf_path)
    parsed = parse_resume(text)
    print(json.dumps(parsed, ensure_ascii=False, indent=2))