from flask import Flask, render_template, request, redirect, url_for
import os
from resume_analyzer import resume_analyzer

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'domain' not in request.form:
        return redirect(request.url)

    file = request.files['file']
    selected_domain = request.form['domain']
    
    if file.filename == '':
        return redirect(request.url)
    
    # Define skill categories
    skill_categories = {
        'Web Development': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'MERN', 'Next.js'],
        'Data Science': ['Python', 'Machine Learning', 'AI', 'NLP', 'Data Analysis', 'SQL'],
        'Mobile Development': ['Flutter', 'React Native', 'Android', 'iOS'],
        'DevOps': ['Docker', 'Kubernetes', 'AWS', 'Azure', 'CI/CD'],
        'Cloud Computing': ['AWS', 'Azure', 'Google Cloud', 'Cloud Security'],
        'Game Development': ['Unity', 'Unreal Engine', 'C#', 'C++', 'Game Design'],
        'UI/UX Design': ['Figma', 'Adobe XD', 'Sketch', 'User Research', 'Prototyping'],
        'Machine Learning': ['TensorFlow', 'PyTorch', 'Scikit-learn', 'Deep Learning', 'Computer Vision'],
        'Cybersecurity': ['Network Security', 'Ethical Hacking', 'Penetration Testing', 'Malware Analysis'],
        'Other': []
    }
    
    ideal_skills = skill_categories.get(selected_domain, [])

    if file and file.filename.endswith('.pdf'):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Analyze the resume
        analysis_result = resume_analyzer(file_path, ideal_skills)

        # Pass the result to result page
        return render_template('result.html', result=analysis_result)
    else:
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
