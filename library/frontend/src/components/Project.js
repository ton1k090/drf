import React from 'react'



const ProjectItem = ({item, deleteProject}) => {
    return (
        <tr>

            <td>{item.title}</td>
            <td>{item.link}</td>
            <td>{item.users}</td>
            <td><button onClick={()=>deleteProject(item.id)} type='button'>Delete</button></td>

        </tr>
    )
}
const ProjectList = ({items, deleteProject}) => {
    return (
        <table>


                <th>TITLE</th>
                <th>LINK</th>
                <th>USERS</th>
                <th></th>

            {items.map((item) => <ProjectItem item={item} deleteProject={deleteProject}/>)}

        </table>
    )
}
export default ProjectList;