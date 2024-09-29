import PyPDF2
import spacy
import matplotlib.pyplot as plt

# Load NLP model
nlp = spacy.load('en_core_web_sm')

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

# Extract skills from resume
def extract_skills(resume_text):
    skills = [
        'HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'MERN', 'Next.js',
        'Python', 'Machine Learning', 'AI', 'NLP', 'Data Analysis', 'SQL',
        'Flutter', 'React Native', 'Android', 'iOS', 'Docker', 'Kubernetes',
        'AWS', 'Azure', 'Google Cloud', 'Cloud Security', 'Unity', 'Unreal Engine',
        'C#', 'C++', 'Game Design', 'Figma', 'Adobe XD', 'Sketch',
        'User Research', 'Prototyping', 'TensorFlow', 'PyTorch', 
        'Scikit-learn', 'Deep Learning', 'Computer Vision', 'Network Security',
        'Ethical Hacking', 'Penetration Testing', 'Malware Analysis'
    ]
    extracted_skills = [skill for skill in skills if skill.lower() in resume_text.lower()]
    return extracted_skills

# Analyze resume and suggest missing skills
def analyze_resume(extracted_skills, ideal_skills):
    missing_skills = set(ideal_skills) - set(extracted_skills)
    suggestions = {}
    for skill in missing_skills:
        suggestions[skill] = f"Consider improving your {skill} skills."
    return suggestions

# Recommend courses based on missing skills
def recommend_courses(missing_skills):
    course_links = {
        'HTML': 'https://www.w3schools.com/html/',
        'CSS': 'https://www.w3schools.com/css/',
        'JavaScript': 'https://www.udemy.com/course/javascript-the-complete-guide-2020-beginner-advanced/',
        'React': 'https://www.udemy.com/course/react-the-complete-guide-incl-redux/',
        'Node.js': 'https://www.udemy.com/course/the-complete-nodejs-developer-course-2/',
        'MERN': 'https://www.udemy.com/course/mern-stack-front-to-back/',
        'Next.js': 'https://www.udemy.com/course/nextjs-dev-to-deployment/',
        'Python': 'https://www.coursera.org/courses?query=python',
        'Machine Learning': 'https://www.udemy.com/topic/machine-learning/',
        'AI': 'https://www.coursera.org/learn/ai-for-everyone',
        'NLP': 'https://www.coursera.org/specializations/natural-language-processing',
        'SQL': 'https://www.udemy.com/course/the-complete-sql-bootcamp/',
        'Flutter': 'https://www.udemy.com/course/flutter-bootcamp-with-dart/',
        'React Native': 'https://www.udemy.com/course/the-complete-react-native-course/',
        'Android': 'https://www.udacity.com/course/android-developer-nanodegree-by-google--nd801',
        'iOS': 'https://www.udacity.com/course/ios-developer-nanodegree--nd003',
        'Docker': 'https://www.udemy.com/course/docker-mastery/',
        'Kubernetes': 'https://www.udemy.com/course/kubernetes-the-practical-guide/',
        'AWS': 'https://aws.amazon.com/training/',
        'Azure': 'https://www.udacity.com/course/azure-cloud-developer-nanodegree--nd9990',
        'Google Cloud': 'https://cloud.google.com/training/',
        'Cloud Security': 'https://www.udacity.com/course/cloud-security-nanodegree--nd063',
        'Unity': 'https://www.udemy.com/course/unitycourse/',
        'Unreal Engine': 'https://www.udemy.com/course/unrealcourse/',
        'C#': 'https://www.udemy.com/course/csharp-tutorial-for-beginners/',
        'C++': 'https://www.udemy.com/course/beginning-c-plus-plus-programming/',
        'Game Design': 'https://www.udemy.com/course/game-design/',
        'Figma': 'https://www.udemy.com/course/figma-for-beginners/',
        'Adobe XD': 'https://www.udemy.com/course/adobe-xd-ux-design-course/',
        'Sketch': 'https://www.udemy.com/course/sketch-for-beginners/',
        'User Research': 'https://www.udemy.com/course/user-research/',
        'Prototyping': 'https://www.udemy.com/course/prototyping/',
        'TensorFlow': 'https://www.udemy.com/course/deep-learning-with-tensorflow/',
        'PyTorch': 'https://www.udemy.com/course/pytorch-tutorial-for-deep-learning/',
        'Scikit-learn': 'https://www.udemy.com/course/machinelearning/',
        'Deep Learning': 'https://www.udemy.com/course/deep-learning-with-python-and-pytorch/',
        'Computer Vision': 'https://www.udemy.com/course/computer-vision-with-python/',
        'Network Security': 'https://www.udemy.com/course/network-security-architecture/',
        'Ethical Hacking': 'https://www.udemy.com/course/ethical-hacking-bootcamp/',
        'Penetration Testing': 'https://www.udemy.com/course/penetration-testing-bootcamp/',
        'Malware Analysis': 'https://www.udemy.com/course/malware-analysis/'
    }
    return {skill: course_links.get(skill, 'No course available') for skill in missing_skills}

# Calculate resume score
def calculate_resume_score(extracted_skills, ideal_skills):
    matched_skills = set(extracted_skills) & set(ideal_skills)
    score = (len(matched_skills) / len(ideal_skills)) * 100
    return score

# Plot skill analysis
def plot_skill_analysis(extracted_skills, ideal_skills):
    matched_skills = len(set(extracted_skills) & set(ideal_skills))
    missing_skills = len(ideal_skills) - matched_skills
    
    labels = ['Matched Skills', 'Missing Skills']
    sizes = [matched_skills, missing_skills]
    colors = ['#4CAF50', '#FF5722']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Resume Skill Match Analysis')
    plt.show()

# Main Resume Analyzer function
def resume_analyzer(pdf_path, ideal_skills):
    resume_text = extract_text_from_pdf(pdf_path)
    extracted_skills = extract_skills(resume_text)
    missing_skills = set(ideal_skills) - set(extracted_skills)
    
    analysis_result = {
        'matched_skills': extracted_skills,
        'missing_skills': missing_skills,
        'suggestions': analyze_resume(extracted_skills, ideal_skills),
        'recommended_courses': recommend_courses(missing_skills),
        'resume_score': calculate_resume_score(extracted_skills, ideal_skills)
    }

    # Uncomment to plot skill analysis
    # plot_skill_analysis(extracted_skills, ideal_skills)

    return analysis_result
