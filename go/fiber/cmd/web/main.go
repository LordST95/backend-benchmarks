package main

import (
	"fmt"

	"github.com/gofiber/fiber/v2"

	"example.com/m/config"
	"example.com/m/internal/app/v1/routes"
)

func main() {
	// Create an instance of AppConfig
	appConfig := config.NewAppConfig()

	// Access configuration values
	port := appConfig.Port

	// Initialize the Fiber app
	app := fiber.New()

	app.Get("/", func(c *fiber.Ctx) error {
		return c.SendString("Hello, World!")
	})
	routes.AuthRoutes(app)

	// Start the Fiber server with the specified port
	err := app.Listen(":" + port)
	if err != nil {
		fmt.Printf("Error starting the server: %v\n", err)
	} else {
		fmt.Printf("Server is running on port %s\n", port)
	}
}
