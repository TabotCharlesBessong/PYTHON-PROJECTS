import { ColorSwatch, Group } from "@mantine/core";
import { Button } from "@/components/ui/button";
import { useEffect, useRef, useState } from "react";
import axios from "axios";
import Draggable from "react-draggable";
import { SWATCHES } from "@/constants";
// import {LazyBrush} from 'lazy-brush';

// Add MathJax type definitions
declare global {
  interface Window {
    MathJax: {
      Hub: {
        Config: (config: any) => void;
        Queue: (commands: any[]) => void;
      };
    };
  }
}

interface GeneratedResult {
  expression: string;
  answer: string;
}

interface Response {
  expr: string;
  result: string;
  assign: boolean;
}

export default function Home() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const draggableRef = useRef<HTMLDivElement>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [color, setColor] = useState("rgb(255, 255, 255)");
  const [reset, setReset] = useState(false);
  const [dictOfVars, setDictOfVars] = useState({});
  const [result, setResult] = useState<GeneratedResult>();
  const [latexPosition, setLatexPosition] = useState({ x: 10, y: 200 });
  const [latexExpression, setLatexExpression] = useState<Array<string>>([]);
  const [mathJaxLoaded, setMathJaxLoaded] = useState(false);

  // const lazyBrush = new LazyBrush({
  //     radius: 10,
  //     enabled: true,
  //     initialPoint: { x: 0, y: 0 },
  // });

  useEffect(() => {
    // Load MathJax
    const script = document.createElement("script");
    script.src = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-MML-AM_CHTML";
    script.async = true;
    script.onload = () => {
      if (window.MathJax) {
        window.MathJax.Hub.Config({
          tex2jax: {
            inlineMath: [["$", "$"], ["\\(", "\\)"]],
            displayMath: [["$$", "$$"], ["\\[", "\\]"]],
          },
          showProcessingMessages: false,
          messageStyle: "none",
        });
        setMathJaxLoaded(true);
      }
    };
    document.head.appendChild(script);

    return () => {
      document.head.removeChild(script);
    };
  }, []);

  useEffect(() => {
    if (latexExpression.length > 0 && mathJaxLoaded && window.MathJax) {
      window.MathJax.Hub.Queue(["Typeset", window.MathJax.Hub]);
    }
  }, [latexExpression, mathJaxLoaded]);

  useEffect(() => {
    if (result) {
      renderLatexToCanvas(result.expression, result.answer);
    }
  }, [result]);

  useEffect(() => {
    if (reset) {
      resetCanvas();
      setLatexExpression([]);
      setResult(undefined);
      setDictOfVars({});
      setReset(false);
    }
  }, [reset]);

  useEffect(() => {
    const canvas = canvasRef.current;

    if (canvas) {
      const ctx = canvas.getContext("2d");
      if (ctx) {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight - canvas.offsetTop;
        ctx.lineCap = "round";
        ctx.lineWidth = 3;
      }
    }
  }, []);

  const renderLatexToCanvas = (expression: string, answer: string) => {
    const latex = `\\(\\LARGE{${expression} = ${answer}}\\)`;
    setLatexExpression(prev => [...prev, latex]);
  };

  const resetCanvas = () => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext("2d");
      if (ctx) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
    }
  };

  const startDrawing = (e: React.MouseEvent<HTMLCanvasElement>) => {
    const canvas = canvasRef.current;
    if (canvas) {
      canvas.style.background = "black";
      const ctx = canvas.getContext("2d");
      if (ctx) {
        ctx.beginPath();
        ctx.moveTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        setIsDrawing(true);
      }
    }
  };
  const draw = (e: React.MouseEvent<HTMLCanvasElement>) => {
    if (!isDrawing) {
      return;
    }
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext("2d");
      if (ctx) {
        ctx.strokeStyle = color;
        ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
        ctx.stroke();
      }
    }
  };
  const stopDrawing = () => {
    setIsDrawing(false);
  };

  const runRoute = async () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    try {
      const response = await axios({
        method: "post",
        url: `${import.meta.env.VITE_API_URL}/calculate`,
        data: {
          image: canvas.toDataURL("image/png"),
          dict_of_vars: dictOfVars,
        },
      });

      const resp = response.data;
      console.log("Response", resp);

      // Update variables if needed
      resp.data.forEach((data: Response) => {
        if (data.assign) {
          setDictOfVars(prev => ({
            ...prev,
            [data.expr]: data.result,
          }));
        }
      });

      // Calculate position for latex
      const ctx = canvas.getContext("2d");
      if (!ctx) return;

      const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
      let minX = canvas.width, minY = canvas.height, maxX = 0, maxY = 0;

      for (let y = 0; y < canvas.height; y++) {
        for (let x = 0; x < canvas.width; x++) {
          const i = (y * canvas.width + x) * 4;
          if (imageData.data[i + 3] > 0) {
            minX = Math.min(minX, x);
            minY = Math.min(minY, y);
            maxX = Math.max(maxX, x);
            maxY = Math.max(maxY, y);
          }
        }
      }

      const centerX = (minX + maxX) / 2;
      const centerY = (minY + maxY) / 2;
      setLatexPosition({ x: centerX, y: centerY });

      // Set results
      resp.data.forEach((data: Response) => {
        setResult({
          expression: data.expr,
          answer: data.result,
        });
      });
    } catch (error) {
      console.error("Error processing image:", error);
    }
  };

  return (
    <>
      <div className="grid grid-cols-3 gap-2">
        <Button
          onClick={() => setReset(true)}
          className="z-20 bg-black text-white"
          variant="default"
          color="black"
        >
          Reset
        </Button>
        <Group className="z-20">
          {SWATCHES.map((swatch) => (
            <ColorSwatch
              key={swatch}
              color={swatch}
              onClick={() => setColor(swatch)}
            />
          ))}
        </Group>
        <Button
          onClick={runRoute}
          className="z-20 bg-black text-white"
          variant="default"
          color="white"
        >
          Run
        </Button>
      </div>
      <canvas
        ref={canvasRef}
        id="canvas"
        className="absolute top-0 left-0 w-full h-full"
        onMouseDown={startDrawing}
        onMouseMove={draw}
        onMouseUp={stopDrawing}
        onMouseOut={stopDrawing}
      />

      {latexExpression &&
        latexExpression.map((latex, index) => (
          <Draggable
            key={index}
            nodeRef={draggableRef}
            defaultPosition={latexPosition}
          >
            <div ref={draggableRef} className="absolute">
              <div dangerouslySetInnerHTML={{ __html: latex }} />
            </div>
          </Draggable>
        ))}
    </>
  );
}
