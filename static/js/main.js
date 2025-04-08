// DOM Elements
const resumeBuilder = document.getElementById('resume-builder');
const apiBaseUrl = '/api';

// Current resume data
let currentResume = null;

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
    loadResumeBuilder();
    setupEventListeners();
});

// Load resume builder interface
function loadResumeBuilder() {
    // Check if user is logged in (you'll implement auth later)
    const userId = localStorage.getItem('userId');
    
    if (userId) {
        fetchUserResumes(userId);
    } else {
        showLoginForm();
    }
}

// Fetch user's resumes from API
async function fetchUserResumes(userId) {
    try {
        const response = await fetch(`${apiBaseUrl}/users/${userId}/resumes`);
        const resumes = await response.json();
        renderResumeList(resumes);
    } catch (error) {
        console.error('Error fetching resumes:', error);
    }
}

// Render resume list
function renderResumeList(resumes) {
    resumeBuilder.innerHTML = `
        <div class="resume-list">
            <h2>Your Resumes</h2>
            <button id="create-resume">Create New Resume</button>
            ${resumes.map(resume => `
                <div class="resume-item" data-id="${resume.id}">
                    <h3>${resume.title}</h3>
                    <p>${resume.summary || 'No summary'}</p>
                    <button class="edit-resume" data-id="${resume.id}">Edit</button>
                    <button class="export-resume" data-id="${resume.id}">Export</button>
                </div>
            `).join('')}
        </div>
    `;
}

// Setup event listeners
function setupEventListeners() {
    document.addEventListener('click', async (e) => {
        if (e.target.id === 'create-resume') {
            await createNewResume();
        } else if (e.target.classList.contains('edit-resume')) {
            const resumeId = e.target.dataset.id;
            editResume(resumeId);
        } else if (e.target.classList.contains('export-resume')) {
            const resumeId = e.target.dataset.id;
            exportResume(resumeId);
        }
    });
}

// Create new resume
async function createNewResume() {
    const title = prompt('Enter resume title:');
    if (!title) return;
    
    const userId = localStorage.getItem('userId');
    try {
        const response = await fetch(`${apiBaseUrl}/resumes`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_id: userId,
                title: title,
                summary: ''
            })
        });
        const newResume = await response.json();
        fetchUserResumes(userId);
    } catch (error) {
        console.error('Error creating resume:', error);
    }
}

// Edit resume
function editResume(resumeId) {
    // Implement resume editor UI
    console.log('Editing resume:', resumeId);
    // You'll expand this with section editing
}

// Export resume
function exportResume(resumeId) {
    window.open(`${apiBaseUrl}/resumes/${resumeId}/export?format=pdf`, '_blank');
}

// Show login form
function showLoginForm() {
    resumeBuilder.innerHTML = `
        <div class="auth-form">
            <h2>Login</h2>
            <form id="login-form">
                <input type="email" placeholder="Email" required>
                <input type="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
            <p>Don't have an account? <a href="#" id="show-register">Register</a></p>
        </div>
    `;
}
