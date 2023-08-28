document.addEventListener("DOMContentLoaded", function () {
  const resultDiv = document.querySelector("#result");
  const predictedSavingsSpan = document.querySelector("#predicted-savings");

  // Check if the result is available in the query parameters
  const urlParams = new URLSearchParams(window.location.search);
  if (urlParams.has("predicted_savings")) {
    const predictedSavings = urlParams.get("predicted_savings");
    predictedSavingsSpan.textContent = predictedSavings;
    resultDiv.style.display = "block";
  }
});
