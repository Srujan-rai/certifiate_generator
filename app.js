document.addEventListener("DOMContentLoaded", () => {
    const certificateInput = document.getElementById("certificate");
    const csvInput = document.getElementById("csvFile");
    const canvas = document.getElementById("certificateCanvas");
    const ctx = canvas.getContext("2d");
    let image = new Image();

    certificateInput.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                image.src = reader.result;
                image.onload = () => {
                    canvas.width = image.width;
                    canvas.height = image.height;
                    ctx.drawImage(image, 0, 0);
                };
            };
            reader.readAsDataURL(file);
        }
    });

    canvas.addEventListener("click", (e) => {
        const rect = canvas.getBoundingClientRect();
        document.getElementById("xCoord").value = e.clientX - rect.left;
        document.getElementById("yCoord").value = e.clientY - rect.top;
    });

    document.getElementById("certificateForm").addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData();
        formData.append("certificate", certificateInput.files[0]);
        formData.append("csvFile", csvInput.files[0]);
        formData.append("xCoord", document.getElementById("xCoord").value);
        formData.append("yCoord", document.getElementById("yCoord").value);
        formData.append("font", document.getElementById("fontSelect").value);
        formData.append("email", document.getElementById("email").value);
        formData.append("password", document.getElementById("password").value);

        const response = await fetch("http://127.0.0.1:5000/generate", {
            method: "POST",
            body: formData,
        });

        const result = await response.json();
        alert(result.message);
    });
});
