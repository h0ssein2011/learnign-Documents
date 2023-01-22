const jobFilter = document.querySelector("#job-filter");
const locationFilter = document.querySelector("#location-filter");
const jobListings = document

fetch("jobs-data.json")
  .then(response => response.json())
  .then(data => {
    // Iterate over the data and create the job listings
    for (let i = 0; i < data.length; i++) {
      const job = data[i];
      const jobListing = document.createElement("div");
      jobListing.classList.add("job-listing");
      jobListing.innerHTML = `<h3 class="job-title">${job.job_title}</
