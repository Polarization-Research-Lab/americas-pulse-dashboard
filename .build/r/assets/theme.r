theme_prl <- function(base_size = 12, base_family = "sans") {
  colors <- deframe(ggthemes::ggthemes_data[["fivethirtyeight"]])
  (theme_foundation(base_size = base_size, base_family = base_family)
    + theme(
      line = element_line(colour = "black"),
      rect = element_rect(
                          linetype = 0, colour = NA),
      text = element_text(colour = colors["Dark Gray"]),
      axis.title = element_text(size = rel(.8)),
      axis.text = element_text(color = colors["Dark Gray"],face = "bold", size = rel(.6)),
      axis.ticks = element_blank(),
      axis.line = element_blank(),
      legend.background = element_rect(),
      legend.position = "bottom",
      legend.direction = "horizontal",
      legend.box = "vertical",
      panel.grid = element_line(colour = NULL),
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank(),
      plot.title = element_text(hjust = 0, size = rel(1.3), face = "bold"),
      plot.margin = unit(c(.5, .5, .5, .5), "lines"),
      strip.text = element_text(face = "bold"),
      plot.caption = element_text(),
      strip.background = element_rect()) 
      )
}

fivethirtyeight_pal <- function() {
  colors <- deframe(ggthemes::ggthemes_data[["fivethirtyeight"]])
  values <- unname(colors[c("Blue", "Red", "Green")])
  max_n <- length(values)
  f <- manual_pal(values)
  attr(f, "max_n") <- max_n
  f
}

#' FiveThirtyEight color scales
#'
#' Color scales using the colors in the FiveThirtyEight graphics.
#'
#' @inheritParams ggplot2::scale_colour_hue
#' @family colour fivethirtyeight
#' @rdname scale_fivethirtyeight
#' @seealso \code{\link{theme_fivethirtyeight}()} for examples.
#' @export
scale_colour_fivethirtyeight <- function(...) {
  discrete_scale("colour", "economist", fivethirtyeight_pal(), ...)
}

#' @rdname scale_fivethirtyeight
#' @export
scale_color_fivethirtyeight <- scale_colour_fivethirtyeight

#' @rdname scale_fivethirtyeight
#' @export
scale_fill_fivethirtyeight <- function(...) {
  discrete_scale("fill", "economist", fivethirtyeight_pal(), ...)
}