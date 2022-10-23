import { Table, ButtonGroup, Button } from 'react-bootstrap';
import { Check, X } from 'react-bootstrap-icons';


export default function StudentTable(props) {
    const students = props.students.sort((a, b) => (a.points < b.points) ? 1 : -1);

    return (
        <>
            <Table striped bordered hover>
                <thead>
                    <tr>
                        <th>Jméno</th>
                        <th>Body</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    { students.map((student) => (
                        <tr key={ student.id }>
                            <td style={{ textDecoration: student.drawed ? 'line-through' : 'none'}}>{ student.name }</td>
                            <td>{ student.points }</td>
                            <td>
                                <ButtonGroup size="sm">
                                    <Button onClick={() => {props.changePoints(student.id, '+')}}><Check /></Button>
                                    <Button onClick={() => {props.changePoints(student.id, '-')}}><X /></Button>
                                </ButtonGroup>
                            </td>
                        </tr>
                    ))}
                </tbody>
                </Table>
        </>
    )
}