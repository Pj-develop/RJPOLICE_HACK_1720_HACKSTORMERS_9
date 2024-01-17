console.log("login.js");

const usernamefield = document.querySelector("#username");
const password = document.querySelector("#password");
const feeddbackfield = document.querySelector(".invalid-feedback");
const feeddbackfield2 = document.querySelector(".invalid-feedback2");
const usernamesuccessfield = document.querySelector(".usernamesuccess");
const loginBtn = document.querySelector("#loginbtn");

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
