"use client";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { SignInButton, useUser, SignOutButton } from "@clerk/nextjs";
import Image from "next/image";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { getAvatar } from "@/lib/get-avatar";
import { COLORS } from "@/lib/constants";

export function Navbar() {
  const { isSignedIn, user } = useUser();

  return (
    <nav
      className={`flex items-center bg-${COLORS.navbar} justify-between p-4 border-b border-zinc-800`}
    >
      <div className="flex items-center space-x-4 hover:cursor-pointer hover:opacity-80">
        <Image src="/logo.png" alt="Logo" width={40} height={40} />
        <Link href="/" className="text-2xl font-bold">
          TaskEase
        </Link>
      </div>

      <div className="flex items-center space-x-4">
        {isSignedIn ? (
          <div className="flex items-center space-x-4">
            <Avatar>
              <AvatarImage src={user.imageUrl || getAvatar()} />
              <AvatarFallback>CN</AvatarFallback>
            </Avatar>
            <span className="text-sm font-medium leading-none">
              {user.firstName}
            </span>
            <div className="text-sm font-medium">
              <SignOutButton>
                <Button
                  variant="ghost"
                  className="cursor-pointer hover:bg-zinc-500 transition-colors duration-200"
                >
                  Sign Out
                </Button>
              </SignOutButton>
            </div>
          </div>
        ) : (
          <SignInButton>
            <Button className="cursor-pointer">Sign In</Button>
          </SignInButton>
        )}
      </div>
    </nav>
  );
}
