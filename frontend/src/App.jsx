import { useState, useEffect } from 'react'
import './App.css'
import ContactList from './ContactList'
import ContactForm from './ContactForm'

function App() {
  const [contacts, setContacts] = useState([{"firstName": "Neev", "lastName": "Bakshi", "email": "bakshi.neev@gmail.com", id: 1}])

  //calls fetch contacts as soon as this component renders
  useEffect(() => {
    fetchContacts()
  }, [])

  //sends request to backend to get contacts, waits for response and stores
  const fetchContacts = async () => {
    const response = await fetch("http://127.0.0.1:5000/contacts")
    const data = await response.json()
    setContacts(data.contacts)
    console.log(data.contacts)
  }

  return (
    <>
    <ContactList contacts={contacts}/>
    <ContactForm />
    </>
  );
  
}

export default App
