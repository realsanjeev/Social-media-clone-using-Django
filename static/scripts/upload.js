const inputImage = document.getElementById("inputImage");
const previewArea = document.getElementById("preview-image");
const placeholder = document.getElementById("placeholder");
// detect upload
inputImage.addEventListener("change", () => {
  const reader = new FileReader();

  reader.readAsDataURL(inputImage.files[0]);

  reader.onload = (e) => {
    const img = document.createElement("img");
    img.src = e.target.result;
    img.classList.add("img");

    placeholder.style.display = "none";
    previewArea.append(img);
  };
});
