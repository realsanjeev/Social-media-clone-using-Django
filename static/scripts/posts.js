const arrows = document.querySelectorAll('.arrow');
const containers = document.querySelectorAll('.image-container');
const bullets = document.querySelector('.bullets');
const leftContainer = containers[0];
const rightContainer = containers[1];

let pendingAnimation = false;
let index = 0;

const imgs = [
  'https://placehold.co/470x585/red/white/?text=A',
  'https://placehold.co/470x585/yellow/black/?text=B',
  'https://placehold.co/470x585/blue/white/?text=C'
];

const updateUI = () => {
  arrows[0].style.visibility = (index > 0) ? 'visible' : 'hidden';
  arrows[1].style.visibility = (index < (imgs.length - 1)) ? 'visible' : 'hidden';
  for (let i = 0; i < bullets.children.length; i++) {
    const bullet = bullets.children[i];
    
    if (i === index) {
      bullet.classList.add('active');
    } else {
      bullet.classList.remove('active');
    }
  }
};


const setLeftImage = (path) => {
  leftContainer.style.backgroundImage = `url(${ path })`;
};

const setRightImage = (path) => {
  rightContainer.style.backgroundImage = `url(${ path })`;
};

const slide = (direction, forcedIndex = false) => {
  if (pendingAnimation) {
    return;
  }
  
  if (!forcedIndex) {
    index += (direction === 'left') ? -1 : 1;
    index = Math.min(Math.max(index, 0), (imgs.length - 1));
    setLeftImage(imgs[direction === 'left' ? index : (index - 1)]);
    setRightImage(imgs[direction === 'left' ? (index + 1) : index]);
  }
  
  //Reset animation
  leftContainer.style.animationName = 'none';
  rightContainer.style.animationName = 'none';
  void leftContainer.offsetWidth;
  void rightContainer.offsetWidth;
  
  leftContainer.style.animationName = (direction === 'left') ? 'leftIn' : 'leftOut';
  rightContainer.style.animationName = (direction === 'left') ? 'rightOut' : 'rightIn';
  
  pendingAnimation = true;
  updateUI();
}

const setCurrentIndex = (imgIndex) => {
  const direction = (imgIndex < index) ? 'left' : 'right';
  const tempIndex = index;
  
  if (imgIndex === index) {
    return ;
  }
  
  index = imgIndex;
  setLeftImage(imgs[direction === 'left' ? index : tempIndex]);
  setRightImage(imgs[direction === 'left' ? tempIndex : index]);
  slide(direction, true);
};
                
leftContainer.style.backgroundImage = `url(${ imgs[index] })`;
rightContainer.style.backgroundImage = `url(${ imgs[index] })`;
arrows.forEach(arrow => arrow.addEventListener('click', () => slide(arrow.dataset.direction)));
containers.forEach(container => container.addEventListener('animationend', () => pendingAnimation = false));
for (let i = 0; i < bullets.children.length; i++) {
  bullets.children[i].addEventListener('click', () => setCurrentIndex(i));
}
updateUI();