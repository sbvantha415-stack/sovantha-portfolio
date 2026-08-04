// 1. Function to fetch and load a project HTML file
async function loadProject(filename, el) {
  // Remove active state from all sidebar items
  document.querySelectorAll('.project-item').forEach(i => i.classList.remove('active'));
  
  // Add active state to the clicked item
  if (el) el.classList.add('active');

  const frame = document.getElementById('demo-frame');
  
  if (frame) {
    // Fade out the iframe
    frame.style.opacity = '0';
    
    try {
      // Fetch the HTML file from the projects folder
      const response = await fetch(`projects/${filename}.html`);
      
      // If the file exists, get its text content (the HTML code)
      if (response.ok) {
        const htmlContent = await response.text();
        
        setTimeout(() => {
          // Inject the HTML into the iframe
          frame.srcdoc = htmlContent;
          // Fade it back in
          setTimeout(() => { frame.style.opacity = '1'; }, 100);
        }, 200);
      } else {
        console.error("Project file not found!");
      }
    } catch (error) {
      console.error("Error loading the project:", error);
    }
  }
}

// 2. Device Toggle Logic
function setDevice(type) {
  const frame = document.getElementById('demo-frame');
  if (type === 'mobile') {
    frame.classList.add('mobile-view');
    document.getElementById('btn-mobile').classList.add('active');
    document.getElementById('btn-desktop').classList.remove('active');
  } else {
    frame.classList.remove('mobile-view');
    document.getElementById('btn-desktop').classList.add('active');
    document.getElementById('btn-mobile').classList.remove('active');
  }
}

// 3. Initialize the default view on load
document.addEventListener('DOMContentLoaded', () => {
  loadProject('home', document.getElementById('nav-home'));
});