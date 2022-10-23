console.log("running")

const nameValidate = () => {
    const userData = document.forms['quote_form']

    const firstNameFormElement = userData['first_name']
    const firstName = firstNameFormElement.value

    const lastNameFormElement = userData['last_name']
    const lastName = lastNameFormElement.value

    if (firstName.length < 3) {
        firstNameFormElement.setCustomValidity('First name must be atleast 3 characters')
        firstNameFormElement.reportValidity()
    }
    
    if (lastName.length < 3) {
        lastNameFormElement.setCustomValidity('Last name must be atleast 3 characters')
        lastNameFormElement.reportValidity()
    }

}


const emailValidate = () => {
    const userData = document.forms['quote_form']

    const emailFormElement = userData['email']
    const email = emailFormElement.value

    if (email.length < 5) {
        emailFormElement.setCustomValidity('Email must be atleast 5 characters')
        emailFormElement.reportValidity()
    }

}

const phoneValidate = () => {
    const userData = document.forms['quote_form']
    const phoneFormElement = userData['phone']
    const phone = phoneFormElement.value

    if (phone.length < 3) {
        phoneFormElement.setCustomValidity(' must be atleast 3 characters')
        phoneFormElement.reportValidity()
    }
}
