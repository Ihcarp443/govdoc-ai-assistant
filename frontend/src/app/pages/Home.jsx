import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card } from "@/components/ui/cards";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogDescription, DialogTrigger } from "@/components/ui/dialog";
import { Label } from "@/components/ui/label";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { Upload, Image as  Sparkles, FileSearch, Shield, Zap } from "lucide-react";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
// import { Label } from "@/components/ui/label";
import { login, signup } from "../Services/auth";

const Home = () => {
  const [open, setOpen] = useState(false);
  const [role, setRole] = useState("public");
  const [signinEmail, setSigninEmail] = useState("");
  const [signinPassword, setSigninPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const [signupEmail, setSignupEmail] = useState("");
  const [signupPassword, setSignupPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const router = useRouter();
  const handleLogin = async () => {
  try {
      const response = await login(signinEmail, signinPassword);

      if (response.success) {
        localStorage.setItem("user", JSON.stringify(response.user));

        alert("Login Successful");

        setOpen(false);
      } else {
        alert(response.detail);
      }
    } catch (err) {
      console.error(err);
      alert("Login Failed");
    }
  };

  const handleSignup = async () => {
    if (signupPassword !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      const response = await signup(
        signupEmail,
        signupPassword,
        fullName
      );

      if (response.success) {
        alert("Signup Successful");

        setOpen(false);
      } else {
        alert(response.detail);
      }
    } catch (err) {
      console.error(err);
      alert("Signup Failed");
    }
  };

  return (
    <div className="min-h-screen w-full bg-gradient-to-br from-background via-background to-primary/5 flex flex-col">
      <header className="border-b border-border/50 backdrop-blur-sm bg-background/80 sticky top-0 z-40">
        <div className="w-full mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="h-8 w-8 rounded-lg bg-primary flex items-center justify-center">
              <FileSearch className="h-5 w-5 text-primary-foreground" />
            </div>
            <span className="font-bold text-xl">DocuChat AI</span>
          </div>
          <Dialog open={open} onOpenChange={setOpen}>
            <DialogTrigger asChild>
              <Button className={"cursor-pointer"}>Get Started</Button>
            </DialogTrigger>
            <DialogContent className="sm:max-w-[425px]">
              <DialogHeader>
                <DialogTitle>Welcome to DocuChat AI</DialogTitle>
                <DialogDescription>
                  Sign in to your account or create a new one to get started.
                </DialogDescription>
              </DialogHeader>
              <Tabs defaultValue="signin" className="w-full">
                <TabsList className="grid w-full grid-cols-2">
                  <TabsTrigger value="signin">Sign In</TabsTrigger>
                  <TabsTrigger value="signup">Sign Up</TabsTrigger>
                </TabsList>
                <TabsContent value="signin" className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="signin-email">Email</Label>
                    {/* <Input id="signin-email" type="email" placeholder="you@example.com" /> */}
                    <Input
                        type="email"
                        value={signinEmail}
                        onChange={(e) => setSigninEmail(e.target.value)}
                        placeholder="you@example.com"
                      />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="signin-password">Password</Label>
                    <Input
                        type="password"
                        value={signinPassword}
                        onChange={(e) => setSigninPassword(e.target.value)}
                      />
                    {/* <Input id="signin-password" type="password" placeholder="••••••••" /> */}
                  </div>
                <div className="space-y-3">
                    <Label>Role</Label>
                    <RadioGroup
                      value={role}
                      onValueChange={setRole}
                      className="flex gap-6"
                    >
                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="public" id="public" />
                        <Label htmlFor="public">Public</Label>
                          </div>

                      <div className="flex items-center space-x-2">
                        <RadioGroupItem value="admin" id="admin" />
                        <Label htmlFor="admin">Admin</Label>
                      </div>
                    </RadioGroup>
                  </div>
                  {/* <Button className="w-full" onClick={() => setOpen(false)}>Sign In</Button> */}
                  <Button className="w-full" onClick={handleLogin}>
                        Sign In
                      </Button>
                  
                  {/* <p className="text-xs text-center text-muted-foreground">
                    Forgot password? <a href="#" className="text-primary hover:underline">Reset here</a>
                  </p> */}
                </TabsContent>
                <TabsContent value="signup" className="space-y-4">
                  <div className="space-y-2">
                    <Label htmlFor="signup-name">Full Name</Label>
                    <Input
                      id="signup-name"
                      placeholder="John Doe"
                      value={fullName}
                      onChange={(e) => setFullName(e.target.value)}
                    />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="signup-email">Email</Label>
                    <Input
                      type="email"
                      value={signupEmail}
                      onChange={(e) => setSignupEmail(e.target.value)}
                      placeholder="you@example.com"
                    />
                    {/* <Input id="signup-email" type="email" placeholder="you@example.com" /> */}
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="signup-password">Password</Label>
                    <Input
                        type="password"
                        value={signupPassword}
                        onChange={(e) => setSignupPassword(e.target.value)}
                      />
                    {/* <Input id="signup-password" type="password" placeholder="••••••••" /> */}
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="signup-confirm">Confirm Password</Label>
                    <Input
                        type="password"
                        value={confirmPassword}
                        onChange={(e) => setConfirmPassword(e.target.value)}
                      />
                    {/* <Input id="signup-confirm" type="password" placeholder="••••••••" /> */}
                  </div>

                  {/* <Button className="w-full" onClick={() => setOpen(false)}>Create Account</Button>*/}
                  <Button className="w-full" onClick={handleSignup}>
                    Create Account
                  </Button> 
                  <p className="text-xs text-center text-muted-foreground">
                    By signing up, you agree to our <a href="#" className="text-primary hover:underline">Terms</a> and <a href="#" className="text-primary hover:underline">Privacy Policy</a>
                  </p>
                </TabsContent>
              </Tabs>
            </DialogContent>
          </Dialog>
        </div>
      </header>

      <main className="flex-1 flex items-center justify-center px-4 sm:px-6 lg:px-8">
        <div className="max-w-4xl w-full text-center space-y-8">
          <div className="space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-primary/10 text-primary text-sm font-medium">
              <Sparkles className="h-4 w-4" />
              AI-Powered Document Analysis
            </div>
            <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold tracking-tight text-foreground">
              Chat with Your Documents
            </h1>
            <p className="text-lg sm:text-xl text-muted-foreground max-w-2xl mx-auto">
              Upload PDFs, images, and documents. Ask questions and get instant, intelligent answers powered by AI.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Dialog open={open} onOpenChange={setOpen}>
              <DialogTrigger asChild>
                <Button size="lg" className="text-lg px-8 cursor-pointer">
                  Get Started Free
                </Button>
              </DialogTrigger>
            </Dialog>
            <Button  size="lg" variant="outline" className="cursor-not-allowed text-lg px-8">
              Instructions
            </Button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-6 mt-16">
            <Card className="p-6 space-y-3 border-border/50">
              <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mx-auto">
                <Upload className="h-6 w-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg">Easy Upload</h3>
              <p className="text-sm text-muted-foreground">
                Drag and drop your documents or select files from your device.
              </p>
            </Card>
            <Card className="p-6 space-y-3 border-border/50">
              <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mx-auto">
                <Zap className="h-6 w-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg">Instant Answers</h3>
              <p className="text-sm text-muted-foreground">
                Get intelligent responses to your questions in seconds.
              </p>
            </Card>
            <Card className="p-6 space-y-3 border-border/50">
              <div className="h-12 w-12 rounded-lg bg-primary/10 flex items-center justify-center mx-auto">
                <Shield className="h-6 w-6 text-primary" />
              </div>
              <h3 className="font-semibold text-lg">Secure & Private</h3>
              <p className="text-sm text-muted-foreground">
                Your documents are safe and secure as we never shared with third parties.
              </p>
            </Card>
          </div>
        </div>
      </main>

      <footer className="border-t border-border/50 py-6">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-sm text-muted-foreground">
          <p>Your own AI powered DocChatAI</p>
        </div>
      </footer>
    </div>
  );
};


export default Home