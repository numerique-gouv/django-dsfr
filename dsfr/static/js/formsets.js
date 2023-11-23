// For formsets, add forms and remove forms

let formsetGroup = document.querySelectorAll(".formset");  // Array of each form in the formset
let container = document.querySelector(".formset-group");  // The formset containing all the forms
let addButton = document.querySelector("#add-form");  // Button to add a new form
let totalForms = document.querySelector('[id$="-TOTAL_FORMS"]');  // Total number of forms in formset.management

try {
	let checkbox_remove = document.querySelector('[id$="-DELETE"]');  // Checkbox to remove the formset, not used because replaced with a deleting link
	if ( typeof checkbox_remove !== "undefined" ) {
		let div_remove = checkbox_remove.parentElement.parentElement;
		div_remove.remove();
	}
}
catch (error) {}

let firstForm = formsetGroup[0].cloneNode(true); // Clone the formset

addButton.addEventListener('click', addForm);

function addForm(e) {
	// Add a form to the formset

    e.preventDefault();

	let newForm
	if (formsetGroup[0]){
		newForm = formsetGroup[0].cloneNode(true);  // Clone the formset
	} else {
		newForm = firstForm;  // If all other forms have been deleted
	}

	// Regex
    let formRegex = /\w+-(\d+)-/g;  // Regex to find all instances of the form number
	let idRemoveFormRegex = /remove-(\d+)/g;  // Regex to find all instances of the form number on remove link
	let idRemoveFunctionRegex = /removeFormset\((\d+)\)/g;  // Regex to find all instances of the form number on remove function in link

	// Get the number of the last form on the page
	formsetGroup = document.querySelectorAll(".formset");

	let last_number = 0;
	if (formsetGroup.length > 0){
		let last_form = formsetGroup[formsetGroup.length-1];  // Get the last form in the formset
		last_number = /\w+-(\d+)-\w+/.exec(last_form.innerHTML)[1];  // Get the form number in the last form with a regex (fields in the form have an id following the pattern "form-X-...." where X is the number of the form)
	}


	let newNumber = parseInt(last_number)+1;  // Number of the new form

	// Replace last number by new number in newForm
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${newNumber}-`);  // Update the new form to have the correct form number
    newForm.setAttribute('id', `formset-${newNumber}`);  // Update the new form to have the correct form id
	newForm.innerHTML = newForm.innerHTML.replace(idRemoveFormRegex, `remove-${newNumber}`);  // Update the new form to have the correct form number on remove link
	newForm.innerHTML = newForm.innerHTML.replace(idRemoveFunctionRegex, `removeFormset(${newNumber})`);  // Update the new form to have the correct form number on remove function in link

	// Insert the new form at the end of the list of forms
	container.insertBefore(newForm, addButton);

	// Update total number of forms in the management form
    totalForms.setAttribute('value', `${formsetGroup.length+1}`);

    // Delete the checkbox "Supprimer" since we use a button "Supprimer cet élément"
    try {
        let id_to_delete = document.querySelector('[id$="-DELETE"]').id;
        let to_delete = document.getElementById(id_to_delete);
        to_delete = to_delete.parentNode;
        to_delete.remove();
    } catch { };

}

function removeFormset(numFormset){
    // Remove a form from the formset thanks to the form id

	// Get the form by its id
    let form_id = "formset-" + numFormset;
    let form = document.getElementById(form_id);

	// Remove the form from the formset
    form.remove();

	// Update total number of forms in the management form
	formsetGroup = document.querySelectorAll(".formset");
    totalForms.setAttribute('value', `${formsetGroup.length}`);
}
