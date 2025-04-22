
import './App.css'
import { Button } from './components/ui/button'

function App() {

  return (
    <div className="bg-red-400 w-[100vw] h-[100vh] flex items-center justify-center">
      <p className="text-3xl text-bold text-white">
        Hello world
      </p>
      <Button>Hello</Button>
    </div>
  )
}

export default App
