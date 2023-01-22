const filterButton = document.getElementById("filter-button");
filterButton.addEventListener("click", function() {
  const jobFilter = document.getElementById("job-filter").value.toLowerCase();
  const locationFilter = document.getElementById("location-filter").value.toLowerCase();
  const jobListings = document.querySelectorAll(".job-listing");

  jobListings.forEach(function(jobListing) {
    const jobTitle = jobListing.querySelector(".job-title").textContent.toLowerCase();
    const jobLocation = jobListing.querySelector(".job-location").textContent.toLowerCase();

    if (jobTitle.indexOf(jobFilter) === -1 || jobLocation.indexOf(locationFilter) === -1) {
      jobListing.style.display = "none";
    } else {
      jobListing.style.display = "block";
    }
  });
});


fetch("jobs-data.json")
  .then(response => response.json())
  .then(data => {
    // Iterate over the data and create the job listings
    for (let i = 0; i < data.length; i++) {
      const job = data[i];
      const jobListing = document.createElement("div");
      jobListing.classList.add("job-listing");
      jobListing.innerHTML = `
        <h3 class="job-title">${job.job_title}</h3>
        <div class="job-details">
          <span class="job-location">${job.location}</span>
          <p class="job-description">${job.description}</p>
          <a href="${job.apply_url}" class="apply-button">Apply Now</a>
        </div>
      `;
      document.getElementById("job-listings").appendChild(jobListing);
    }
  })
  .catch(error => console.error("Error:", error));
