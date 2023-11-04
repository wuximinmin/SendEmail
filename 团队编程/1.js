document.getElementById("uploadForm").addEventListener("submit", function (e) {
  e.preventDefault(); // 阻止表单的默认提交行为
  const formData = new FormData(); // 创建一个FormData对象
  const fileInput = document.getElementById("excelFile");
  // 设置窗口的宽度和高度
  window.resizeTo(800, 600); // 将窗口宽度设置为800像素，高度设置为600像素
  if (fileInput.files.length > 0) {
    // 将选定的文件添加到FormData对象
    formData.append("excelFile", fileInput.files[0]);

    // 使用fetch API将FormData发送到服务器
    fetch("/upload-excel", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        // 处理来自服务器的响应
        document.getElementById("message").textContent = data.message;
      })
      .catch((error) => {
        console.error("上传出错: " + error);
      });
  }
});

