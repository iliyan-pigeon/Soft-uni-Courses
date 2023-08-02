function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchField = document.getElementById("searchField")
      let allRows = Array.from(document.querySelectorAll("tbody tr"))

      for (let row of allRows){
         row.classList.remove("select")
         if(row.textContent.trim().includes(searchField.value)){
            row.classList.add("select")
         }
      }

      searchField.value = ""
   }
}