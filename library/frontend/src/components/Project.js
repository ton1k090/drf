import React from 'react'



const ProjectItem = ({item}) => {
    return (
        <tr>

            <td>{item.title}</td>
            <td>{item.link}</td>
            <td>{item.users}</td>
        </tr>
    )
}
const ProjectList = ({items}) => {
    return (
        <table>


                <th>TITLE</th>
                <th>LINK</th>
                <th>USERS</th>

            {items.map((item) => <ProjectItem item={item}/>)}
        </table>
    )
}
export default ProjectList;