
<!DOCTYPE html>
<html>
<head>
    <title>Class21</title>
</head>
<body>
    <center>
        <h1>Grade 10 Class Results</h1>
        <form id="result-form">
            <legend>
                <h2>Student Name</h2>
                <input type="text" placeholder="Enter the student name" id="name">
                <br>
                <h2>Student Marks</h2>
                <input type="number" placeholder="Enter the student score" id="marks">
                <br>
                <button type="submit">Add Results</button>
            </legend>
        </form>

        <section>
            <h3>Results</h3>
            <div id="results-container"></div> <!-- ✅ Fixed id -->
        </section>

        <script>
            document.addEventListener("DOMContentLoaded", () => {
                const form = document.getElementById("result-form");
                const resultsContainer = document.getElementById("results-container"); // ✅ Fixed variable

                const loadResults = () => {
                    const results = JSON.parse(localStorage.getItem("results")) || [];
                    resultsContainer.innerHTML = "";
                    results.forEach(result => {
                        const resultDiv = document.createElement("div");
                        resultDiv.classList.add("result-item");
                        resultDiv.innerHTML = `<span>${result.name}</span> - <span>${result.marks}</span>`;
                        resultsContainer.appendChild(resultDiv);
                    });
                };

                form.addEventListener('submit', (e) => {
                    e.preventDefault();
                    const name = form.name.value.trim();
                    const marks = form.marks.value.trim();

                    if (name && marks) {
                        const results = JSON.parse(localStorage.getItem('results')) || [];
                        results.push({ name, marks });
                        localStorage.setItem('results', JSON.stringify(results));
                        loadResults();
                        form.reset();
                    }
                });

                loadResults();
            });
        </script>
    </center>
</body>
</html>





