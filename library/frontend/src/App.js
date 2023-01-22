import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from "./components/Author";
import axios from "axios";
import {HashRouter, Route, Link, BrowserRouter, Switch, Redirect} from "react-router-dom";
import Project from "./components/Project";
import ProjectList from "./components/Project";
import TodoList from "./components/Todo";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}



class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': [],
            'projects': [],
            'todos': []
        }
    }

    componentDidMount() {

        axios.get('http://127.0.0.1:8000/api/todo')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/project')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects
                    }
                )
            }).catch(error => console.log(error))


        axios.get('http://127.0.0.1:8000/api/authors')
            .then(response => {
                const authors = response.data.results
                this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div>
                {/*<AuthorList authors={this.state.authors}/>*/}
                <BrowserRouter>

                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Authors</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todos</Link>
                            </li>
                        </ul>
                    </nav>


                    <Switch>
                        <Route exact path='/' component={() => <AuthorList items={this.state.authors} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} />} />
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} />} />
                        <Redirect from='/authors' to='/' />
                        <Route component={NotFound404} />
                    </Switch>


                </BrowserRouter>

            </div>
        )
    }
}
export default App;