<template>
  <v-data-table :headers="headers" :items="books">
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Library Mangament Systme</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog max-width="700" v-model="dialog">
          <template v-slot:activator="{ props }">
            <v-btn
              v-bind="props"
              color="blue"
              text="Add Book"
              variant="flat"
            ></v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span>{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-text-field
                v-model="newBook.title"
                label="Title"
              ></v-text-field>
              <v-text-field
                v-model="newBook.author"
                label="Author"
              ></v-text-field>
              <v-text-field
                v-model="newBook.genre"
                label="Genre"
              ></v-text-field>
              <v-text-field v-model="newBook.ISBN" label="ISBN"></v-text-field>
              <v-text-field
                v-model="newBook.pub_year"
                label="Publish Year"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="close">
                Cancel
              </v-btn>
              <v-btn color="blue-darken-1" variant="text" @click="addBook">
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this book?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue-darken-1" variant="text" @click="deleteCancel"
                >Cancel</v-btn
              >
              <v-btn color="blue-darken-1" variant="text" @click="deleteConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:[`item.actions`]="{ item }">
      <v-btn color="green-darken-1" v-bind="props" @click="editBook(item)">
        edit
      </v-btn>
      <v-btn color="red-darken-1" @click="deleteBook(item)"> delete </v-btn>
    </template>
  </v-data-table>
</template>

<script>
import axios from "axios";

export default {
  name: "booksApp",
  data() {
    return {
      headers: [
        {
          title: "Book ID",
          sortable: false,
          key: "_id",
        },
        { title: "Title", key: "title" },
        { title: "Author", key: "author" },
        { title: "ISBN", key: "ISBN" },
        { title: "Genre", key: "genre", sortable: false },
        { title: "Publication year", key: "pub_year" },
        { title: "Actions", key: "actions" },
      ],
      books: [],
      dialog: false,
      dialogDelete: false,
      editForm: false,
      bookID: "",
      newBook: {
        title: "",
        author: "",
        genre: "",
        ISBN: "",
        pub_year: "",
      },
    };
  },
  computed: {
    formTitle() {
      if (this.editForm == true) {
        return "Edit Book";
      } else {
        return "Add Book";
      }
    },
  },
  methods: {
    getBooks() {
      const path = "http://127.0.0.1:5000/books/";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.books = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    close() {
      this.dialog = false;
    },
    addBook() {
      this.dialog = true;
      this.editForm = false;
      const path = "http://127.0.0.1:5000/books/";
      axios
        .post(path, this.newBook)
        .then((res) => {
          console.log(res);
          this.getBooks();
          this.close();
        })
        .catch((err) => {
          console.error(err);
        });
    },

    deleteBook(book) {
      this.dialogDelete = true;
      this.bookID = book["_id"];
    },
    deleteConfirm() {
      const path = "http://127.0.0.1:5000/books/" + this.bookID;
      axios
        .delete(path)
        .then((res) => {
          console.log(res);
          this.getBooks();
          this.deleteCancel();
        })
        .catch((err) => {
          console.error(err);
        });
    },
    deleteCancel() {
      this.dialogDelete = false;
    },
    editBook(book) {
      this.editForm = true;
      this.dialog = true;
      const path = "http://127.0.0.1:5000/books/" + book["_id"];
      this.newBook = book;
      axios
        .put(path, this.newBook)
        .then((res) => {
          console.log(res);
          this.getBooks();
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
