const formUpload = document.getElementById("upload-form");
const titleUpload = document.getElementById("upload-title");
const descriptionUpload = document.getElementById("upload-description");
const fileUpload = document.getElementById("upload-file");
const submitFile = document.getElementById("submit-file");

const progressBox = document.getElementById("progress-box");
const cancelBox = document.getElementById("cancel-box");
const cancelBtn = document.getElementById("cancel-btn");

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
