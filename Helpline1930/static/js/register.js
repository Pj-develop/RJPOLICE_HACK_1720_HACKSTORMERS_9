console.log("reister.js");

const usernamefield = document.querySelector("#username");
const emailfield = document.querySelector("#email");
const password = document.querySelector("#password");
const feeddbackfield = document.querySelector(".invalid-feedback");
const feeddbackfield2 = document.querySelector(".invalid-feedback2");
const usernamesuccessfield = document.querySelector(".usernamesuccess");
const submitBtn = document.querySelector("#submitbtn");

usernamefield.addEventListener("keyup", (e) => {
  usernamefield.classList.remove("is-invalid");
  feeddbackfield.style.display = "none";
  usernamesuccessfield.style.display = "block";
  usernamesuccessfield.textContent = `Checking ${usernamefield.value}`;

  if (usernamefield.value.length > 3) {
    const usernameVal = e.target.value;

    fetch("/auth/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        //console.log("data", data);
        usernamesuccessfield.style.display = "none";

        if (data.username_error) {
          usernamefield.classList.add("is-invalid");
          feeddbackfield.innerHTML = `<p>${data.username_error}</p>`;
          feeddbackfield.style.display = "block";
          submitBtn.disabled = true;
          submitBtn.setAttribute("disabled", "disabled");
        } else {
          submitBtn.removeAttribute("disabled");
          submitBtn.disabled = false;
        }
      });

    //console.log(usernamefield.value);
  } else {
    usernamefield.classList.remove("is-invalid");
  }
});

emailfield.addEventListener("keyup", (e) => {
  emailfield.classList.remove("is-invalid");
  feeddbackfield2.style.display = "none";

  //console.log("EMAIL", email.value);

  if (emailfield.value.length > 3) {
    const emailVal = e.target.value;

    fetch("/auth/validate-email", {
      body: JSON.stringify({ email: emailVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        //console.log("data", data);
        if (data.email_error) {
          submitBtn.setAttribute("disabled", "disabled");
          submitBtn.disabled = true;
          emailfield.classList.add("is-invalid");
          feeddbackfield2.innerHTML = `<p>${data.email_error}</p>`;
          feeddbackfield2.style.display = "block";
        } else {
          submitBtn.removeAttribute("disabled");
        }
      });

    //console.log(username.value);
  } else {
    emailfield.classList.remove("is-invalid");
  }
});
