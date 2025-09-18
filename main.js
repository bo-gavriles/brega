<script>
  // -------------------
  // POPUP — "Leave your contact"
  // -------------------
  const popup = document.getElementById("popupForm");
  const openPopupBtn = document.getElementById("openPopup");
  const closePopupBtn = document.getElementById("closePopup");

  openPopupBtn.onclick = () => popup.style.display = "block";
  closePopupBtn.onclick = () => popup.style.display = "none";

  document.getElementById("leadForm").onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    try {
      await fetch("/api/lead", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
      });
      // можно показать сообщение успеха
      alert("Thank you! We received your contact.");
      popup.style.display = "none";
      // redirect к форме добавления лодки
      window.location.href = "/add-boat-form";
    } catch (err) {
      console.error(err);
      alert("Something went wrong, please try again.");
    }
  };

  // -------------------
  // MODAL — "Quick booking request"
  // -------------------
  const modal = document.getElementById("modal");
  const openBookingBtn = document.getElementById("openBooking");
  const closeModalBtn = document.getElementById("closeModal");

  openBookingBtn.onclick = () => modal.style.display = "block";
  closeModalBtn.onclick = () => modal.style.display = "none";

  document.getElementById("bookingForm").onsubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    const data = Object.fromEntries(formData.entries());

    try {
      await fetch("/api/booking", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
      });
      alert("Your booking request has been sent!");
      modal.style.display = "none";
      e.target.reset(); // очистка формы
    } catch (err) {
      console.error(err);
      alert("Failed to send request. Try again later.");
    }
  };

  // -------------------
  // Закрытие модалок по клику вне содержимого
  // -------------------
  window.onclick = (e) => {
    if (e.target === popup) popup.style.display = "none";
    if (e.target === modal) modal.style.display = "none";
  };
</script>
