const dropArea = document.getElementById('drop-area');
const droppedContent = document.getElementById('dropped-content');

dropArea.addEventListener('dragenter', preventDefaults, false);
dropArea.addEventListener('dragover', preventDefaults, false);
dropArea.addEventListener('dragleave', handleDragLeave, false);
dropArea.addEventListener('drop', handleDrop, false);

dropArea.addEventListener('dragenter', highlight, false);
dropArea.addEventListener('dragover', highlight, false);
dropArea.addEventListener('dragleave', unhighlight, false);
dropArea.addEventListener('drop', unhighlight, false);
dropArea.addEventListener('click', openFileDialog, false);

function preventDefaults(event) {
  event.preventDefault();
  event.stopPropagation();
}

function highlight() {
  dropArea.classList.add('highlight');
  dropArea.innerHTML = `
  <div class="drop-icon">
    <i class="fa-light fa-file-upload"></i>
  </div>
  <div class="drop-text">Drop files</div>
  `; // Add this line
}

function unhighlight() {
  dropArea.classList.remove('highlight');
  dropArea.innerHTML = `
  <div class="drop-icon">
    <i class="fa-light fa-file-upload"></i>
  </div>
  <div class="drop-text">Drag and drop files here</div>
  `;
}

function handleDragLeave(event) {
  if (event.relatedTarget !== null) {
    return;
  }
  unhighlight();
}

function handleDrop(event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  const reader = new FileReader();

  reader.readAsText(file);
  reader.onload = function () {
    droppedContent.value = reader.result;
  };

  unhighlight();
}

function openFileDialog(event) {
  const fileInput = document.createElement('input');
  fileInput.type = 'file';
  fileInput.accept = 'text/plain';

  fileInput.addEventListener('change', handleFileSelect, false);

  fileInput.click();
}

function handleFileSelect(event) {
  const file = event.target.files[0];
  const reader = new FileReader();

  reader.readAsText(file);
  reader.onload = function() {
    droppedContent.value = reader.result;
  };
}

const chars = document.getElementById('chars');

droppedContent.addEventListener('input', () => {
  chars.innerHTML = `${droppedContent.value.length}/5000`;
});

const outerDot = document.getElementById('outer-dot');
const dot = document.getElementById('dot');
let isSpellcheck = true;

outerDot.addEventListener('click', () => {
  isSpellcheck = !isSpellcheck;
  droppedContent.focus();
  
  if (!isSpellcheck) {
    dot.style.transform = 'none';
    outerDot.style.backgroundColor = '#444';
    droppedContent.spellcheck = false;
  } else {
    dot.removeAttribute('style');
    outerDot.removeAttribute('style');
    droppedContent.spellcheck = true;
  }
});