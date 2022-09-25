import './App.css';
import trollFace from './trollface.png';
import { Container, Row, Col, Button, Card } from 'react-bootstrap';
import StudentTable from './components/StudentTable';
import studentsInfo from './students';
import questionsInfo from './questions';
import { useState } from 'react';


function App() {
  const [students, setStudents] = useState(studentsInfo);
  const [questions, setQuestions] = useState(questionsInfo);
  const [selectedQuestion, setSelectedQuestion] = useState();
  const [drawed, setDrawed] = useState('N/A');

  const allDrawed = students.map((student) => {
    return student.drawed ? true : false
  })

  const checker = allDrawed.every(val => val === true);

  if (checker) {
    const studs = students.map((student) => {
      return {...student, drawed: false}
    })
    setStudents(studs);
  }

  const drawQuestion = () => {
    let rand = Math.floor(Math.random() * questions.length);
    while (questions[rand].answered) {
      rand = Math.floor(Math.random() * questions.length);
    }
    
    setSelectedQuestion(questions[rand]);

    const ques = questions.map((question) => {
      return questions[rand].id === question.id ? {...question, answered: true} : question
    })
    setQuestions(ques);
  }

  const drawStudent = () => {
    let rand = Math.floor(Math.random() * students.length);
    while (students[rand].drawed) {
      rand = Math.floor(Math.random() * students.length);
    } 
    setDrawed(students[rand].name);

    const studs = students.map((student) => {
        return students[rand].id === student.id ? {...student, drawed: true} : student
    })

    setStudents(studs);
    drawQuestion()
  }

  const changePoints = (id, operator) => {
    const studs = students.map((student) => {
      if (operator === '+') {
        return student.id === id ? {...student, points: student.points + 1} : student
      } else {
        return student.id === id ? {...student, points: student.points - 1} : student  
      }
    })
    setStudents(studs);
  }

  return (
    <Container style={{ marginTop: 30 }}>
      <Row>
        <Col md={{ span: 6, offset: 3 }} style={{ textAlign: 'center', marginBottom: 60, marginTop: 40 }}>
          <h1>{ drawed }</h1>
            { selectedQuestion ? (<div style={{ marginRight: 15, marginBottom: 10, display: 'inline-block'}}>
            <Card style={{ height: 150, width: 300 }}>
              <Card.Body>
                <Card.Title>#{selectedQuestion.id}</Card.Title>
                <Card.Text>{selectedQuestion.text}</Card.Text>
              </Card.Body>
            </Card>
          </div>) : null}
        </Col>
      </Row>
      <Row>
        <Col md={ 9 } style={{textAlign: 'center'}}>
          { questions.map((question) => {
            return (!question.answered ?
                (
                  <Card key={question.id} style={{ marginRight: 15, marginBottom: 10, display: 'inline-block' }}>
                    <Card.Body>
                      <Card.Title>#{question.id}</Card.Title>
                      <Card.Text>{question.text}</Card.Text>
                    </Card.Body>
                  </Card>)
             : null
            )
          })}
        </Col>
        <Col md={ 3 }>
          <Button onClick={() => { drawStudent() }} style={{ width: '100%', height: '100px', marginBottom: 30, fontSize: '30px'}}>
            <img src={trollFace} alt="face" width="100" />
          </Button>
          <StudentTable students={students} changePoints={changePoints} />
        </Col>
      </Row>
    </Container>
  );
}

export default App;
