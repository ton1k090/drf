import React from 'react'
import Todo from "./Todo";

const TodoItem = ({item}) => {
    return (
        <tr>
            <td>{item.url}</td>
            <td>{item.text}</td>
            <td>{item.created}</td>

        </tr>
    )
}
const TodoList = ({items}) => {
    return (
        <table>

                <th>URL</th>
                <th>TEXT</th>
                <th>CREATED</th>


            {items.map((item) => <TodoItem item={item}/>)}
        </table>
    )
}
export default TodoList;