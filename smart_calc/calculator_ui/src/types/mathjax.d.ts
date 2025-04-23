declare namespace MathJax {
  interface Hub {
    Config(config: any): void;
    Queue(commands: any[]): void;
  }
}

interface Window {
  MathJax: {
    Hub: MathJax.Hub;
  };
} 