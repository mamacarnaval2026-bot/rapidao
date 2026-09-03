const form = document.getElementById("contactForm");

form.addEventListener("submit", function (e) {
  e.preventDefault();

  const name = document.getElementById("name").value.trim();
  const company = document.getElementById("company").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const message = document.getElementById("message").value.trim();

  // Troque pelo número de WhatsApp da sua empresa.
  const whatsapp = "5500000000000";

  const text =
    `Olá, Portal Sim Empresas!%0A%0A` +
    `Nome: ${encodeURIComponent(name)}%0A` +
    `Empresa: ${encodeURIComponent(company || "Não informado")}%0A` +
    `WhatsApp: ${encodeURIComponent(phone)}%0A` +
    `Necessidade: ${encodeURIComponent(message)}`;

  window.open(`https://wa.me/${whatsapp}?text=${text}`, "_blank");
});

document.querySelector(".menu-btn").addEventListener("click", () => {
  const nav = document.querySelector(".desktop-nav");
  nav.style.display = nav.style.display === "flex" ? "none" : "flex";
  nav.style.position = "absolute";
  nav.style.top = "78px";
  nav.style.left = "0";
  nav.style.right = "0";
  nav.style.padding = "20px";
  nav.style.background = "#fff";
  nav.style.flexDirection = "column";
  nav.style.boxShadow = "0 15px 30px #173b5b15";
});
