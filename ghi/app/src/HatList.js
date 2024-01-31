
function HatList(props) {
    return (
        <table>
            <thead>
                <tr>
                    <th>Fabric</th>
                    <th>Style Name</th>
                    <th>Color</th>
                    <th>Location</th>
                </tr>
            </thead>
            <tbody>
                {/* {props.hats.map(hat => {
                    return (
                        <tr key={hat.href}>
                            <td>{hat.fabric}</td>
                            <td>{hat.style_name}</td>
                            <td>{hat.color}</td>
                            <td>{hat.location}</td>
                        </tr>
                    )
                } )} */}
            </tbody>
        </table>
    )
}

export default HatList;
