package routes

import (
	"example.com/m/internal/app/v1/handlers"
	"github.com/gofiber/fiber/v2"
)

func AuthRoutes(app *fiber.App) {
	userRoute := app.Group("/api/v1/auth")

	userRoute.Get("/signin", handlers.Signin)
}
