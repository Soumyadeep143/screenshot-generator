document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const urlInput = document.querySelector("input[name='url']");
    const submitBtn = form.querySelector("button[type='submit']");

    // Create a spinner for feedback
    const spinner = document.createElement("div");
    spinner.classList.add("spinner-border", "text-primary", "mt-3");
    spinner.style.display = "none";
    spinner.setAttribute("role", "status");
    spinner.innerHTML = '<span class="visually-hidden">Loading...</span>';
    form.appendChild(spinner);

    // Handle multiple URLs (batch mode)
    form.addEventListener("submit", (e) => {
        const urls = urlInput.value
            .split(/[\n,]+/)
            .map((u) => u.trim())
            .filter((u) => u.length > 0);

        if (urls.length > 1) {
            e.preventDefault(); // prevent normal form submission

            spinner.style.display = "inline-block";
            submitBtn.disabled = true;

            // Send each URL individually using fetch
            Promise.all(
                    urls.map((url) =>
                        fetch("/", {
                            method: "POST",
                            headers: { "Content-Type": "application/x-www-form-urlencoded" },
                            body: new URLSearchParams({
                                url,
                                format: document.getElementById("format").value,
                                full_page: document.getElementById("full_page").checked ? "on" : "",
                                viewport_width: document.getElementById("viewport_width").value,
                                viewport_height: document.getElementById("viewport_height").value,
                            }),
                        })
                        .then((res) => res.text())
                        .catch((err) => console.error("Error:", err))
                    )
                )
                .then(() => {
                    spinner.style.display = "none";
                    submitBtn.disabled = false;
                    alert("✅ All screenshots captured successfully! Please check your static folder.");
                    location.reload();
                })
                .catch(() => {
                    spinner.style.display = "none";
                    submitBtn.disabled = false;
                    alert("❌ Some screenshots failed to capture. Please try again.");
                });
        } else {
            // Single URL — show spinner normally
            spinner.style.display = "inline-block";
            submitBtn.disabled = true;
        }
    });
});