import React from 'react'
import Todo from "./Todo";
import {Link} from "react-router-dom";

const TodoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>{item.url}</td>
            <td>{item.text}</td>
            <td>{item.created}</td>
            <td><button onClick={()=>deleteTodo(item.id)} type='button'>Delete</button></td>
        </tr>
    )
}
const TodoList = ({items, deleteTodo}) => {
    return (
        <div>
        <table>

                <th>URL</th>
                <th>TEXT</th>
                <th>CREATED</th>


            {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo}/>)}

        </table>
        <Link to='/projects/create'>Create</Link>
        </div>

    )
}
export default TodoList;