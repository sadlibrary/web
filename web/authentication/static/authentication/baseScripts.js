const formUpload = document.getElementById("upload-form");
const titleUpload = document.getElementById("upload-title");
const descriptionUpload = document.getElementById("upload-description");
const fileUpload = document.getElementById("upload-file");
const submitFile = document.getElementById("submit-file");

const progressBox = document.getElementById("progress-box");
const cancelBox = document.getElementById("cancel-box");
const cancelBtn = document.getElementById("cancel-btn");

const formLibrary = document.getElementById("library-form");
const nameLibrary = document.getElementById("library-name");
const descriptionLibrary = document.getElementById("library-description");
const iconLibrary = document.getElementById("library-icon");
const submitLibrary = document.getElementById("submit-library");

const progressBoxLibrary = document.getElementById("progress-box-library");
const cancelBoxLibrary = document.getElementById("cancel-box-library");
const cancelBtnLibrary = document.getElementById("cancel-btn-library");

const csrf = document.getElementsByName("csrfmiddlewaretoken");

librariesDjangoURL = "";
librariesBaseDjangoURL = "";

const asideLibraries = document.getElementById("libraries-box");
asideInnerHtml = `<a
href="#"
class="d-flex align-items-center p-3 link-dark text-decoration-none border-bottom"
disabled
>
<span class="fs-5 fw-semibold">Libraries</span>
</a>
<div
class="list-group list-group-flush border-bottom h-100 overflow-auto"
>`;

// fetch(URL(djangoURL, baseDjangoURL), {
//   headers: {
//     Accept: "application/json",
//     "X-Requested-With": "XMLHttpRequest",
//   },
// }).then((response) => {
//   // return response.json();
//   response = [
//     {
//       name: "new",
//       description: "something",
//       main: true,
//     },
//   ];
//   for (x in response) {
//     asideInnerHtml += `<a
//     href="#"
//     class="list-group-item list-group-item-action active py-3 lh-tight"
//   >
//     <div
//       class="d-flex w-100 align-items-center justify-content-between"
//     >
//       <strong class="mb-1">${x.name}</strong>
//       <small>${x.main ? "Main" : "Created"}</small>
//     </div>
//     <div class="col-10 mb-1 small">
//       ${x.description}
//     </div>
//   </a>`;
//   }
//   asideInnerHtml += `</div>`;
//   asideLibraries.innerHTML = asideInnerHtml;
// });
// //   .then((data) => {
// //     //Perform actions with the response data from the view
// //   });

titleUpload.addEventListener("input", (evt) => {
  const val = titleUpload.value.trim();
  if (val) {
    submitFile.disabled = false;
    fileUpload.disabled = false;
  } else {
    submitFile.disabled = true;
    fileUpload.disabled = true;
  }
});

nameLibrary.addEventListener("input", (evt) => {
  const val = nameLibrary.value.trim();
  if (val) {
    submitLibrary.disabled = false;
  } else {
    submitLibrary.disabled = true;
  }
});

let current_user = "";

fetch("http://127.0.0.1:8000/auth/current_user/", {
  method: "GET",
  headers: {
    Accept: "application/json",
    "X-Requested-With": "XMLHttpRequest",
  },
})
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    current_user = data.username;
    console.log(current_user);
  });

async function addLibrary(url = "", data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

submitLibrary.addEventListener("click", (evt) => {
  evt.preventDefault();
  const data = {
    username: current_user,
    name: nameLibrary.value,
    description: descriptionLibrary.value,
    icon: iconLibrary.value,
    type: "created",
    // csrfmiddlewaretoken: csrf[0].value,
  };
  addLibrary("http://127.0.0.1:8000/library/libraries/", data)
    .then((response) => {
      console.log(response);
      if (response.status == "success") {
        alert("Library added successfully");
        window.location.reload();
      } else {
        alert("Error adding library");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});

fileUpload.addEventListener("change", () => {
  progressBox.classList.remove("d-none");
  cancelBox.classList.remove("d-none");

  const file_data = fileUpload.files[0];
  const url = URL.createObjectURL(file_data);
  console.log(file_data);

  const fd = new FormData();
  //   fd.append("csrfmiddlewaretoken", csrf[0].value);
  fd.append("file", file_data);

  $.ajax({
    type: "POST",
    url: formUpload.action,
    enctype: "multipart/form-data",
    data: fd,
    beforeSend: function () {
      console.log("before");
    },
    xhr: function () {
      const xhr = new window.XMLHttpRequest();
      xhr.upload.addEventListener("progress", (e) => {
        // console.log(e)
        if (e.lengthComputable) {
          const percent = (e.loaded / e.total) * 100;
          console.log(percent);
          progressBox.innerHTML = `<div class="progress">
                                            <div class="progress-bar" role="progressbar" style="width: ${percent}%" aria-valuenow="${percent}" aria-valuemin="0" aria-valuemax="100"></div>
                                        </div>
                                        <p>${percent.toFixed(1)}%</p>`;
        }
      });
      cancelBtn.addEventListener("click", () => {
        xhr.abort();
        setTimeout(() => {
          uploadForm.reset();
          progressBox.innerHTML = "";
          cancelBox.classList.add("d-none");
        }, 2000);
      });
      return xhr;
    },
    success: function (response) {
      console.log(response);
      //   imageBox.innerHTML = `<img src="${url}" width="300px">`;
      //   alertBox.innerHTML = `<div class="alert alert-success" role="alert">
      //                             Successfully uploaded the image below
      //                         </div>`;
      cancelBox.classList.add("d-none");
    },
    error: function (error) {
      console.log(error);
      //   alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
      //                             Oops... something went wrong
      //                         </div>`;
    },
    cache: false,
    contentType: false,
    processData: false,
  });
});
